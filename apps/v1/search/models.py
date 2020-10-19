import os
import requests
from typing import List, Dict


class TMDB(object):
    '''
    Class to wrap TMDB API endpoints into methods for ease of use.
    '''
    empty = [None, '']
    base_url = 'https://api.themoviedb.org/3'
    img_url = 'https://image.tmdb.org/t/p/original'
    search_url = f'{base_url}/search'
    external_id_url = f'{base_url}/find'

    def __init__(self, api_key: str) -> None:
        self.api_key = f'api_key={api_key}'

    def get_movie(self, query: str) -> List[dict]:
        '''
        Returns a list of movies with given query from TMDB API.
        '''
        response: dict = requests.get(
            f'{self.search_url}/movie?query={query}&{self.api_key}'
        ).json()
        results: List[str] = list(response.get('results'))
        return [r for result in results if (r := self._media_result(result, 'movie')) is not None]

    def get_show(self, query: str):
        '''
        Returns a list of movies with given query from TMDB API.
        '''
        response: dict = requests.get(
            f'{self.search_url}/tv?query={query}&{self.api_key}'
        ).json()
        results = response.get('results')
        return [r for result in results if (r := self._media_result(result, 'tv')) is not None]

    def get_media(self, query: str, media_type='movie' or 'tv'):
        return self.get_movie(query) if media_type == 'movie' else self.get_show(query)

    def get_media_from_id(self, imdb_id) -> dict:
        '''
        Returns a list of movies with given IMDB ID from TMDB API.
        '''
        response: dict = requests.get(
            f'{self.external_id_url}/{imdb_id}?external_source=imdb_id&{self.api_key}'
        ).json()

        results = response.get('movie_results')
        media_type = 'movie'

        if results is None or len(results) == 0:
            results = response.get('tv_results')
            media_type = 'tv'

        if results is not None and len(results) > 0:
            return self._media_result(results[0], media_type)
        else:
            return {}

    def get_subtitles(self, imdb_id: str, language: str) -> List[dict]:
        subtitles_url = 'https://rest.opensubtitles.org/search'
        headers = {'User-Agent': 'TemporaryUserAgent'}

        try:
            data: List[dict] = requests.get(
                f'{subtitles_url}/imdbid-{imdb_id}',
                headers=headers
            ).json()
        except:
            data = []

        available_langs = []
        subtitles: List[dict] = []

        for result in data:

            lang_id = result.get('SubLanguageID')

            if lang_id is not None and lang_id not in available_langs:
                available_langs.append(lang_id)

            if (lang_id is None or lang_id != language) and language != 'all':
                continue

            current = {
                'file_name': result.get('SubFileName'),
                'language': lang_id,
                'download_url': result.get('SubDownloadLink')
            }
            if result.get('MovieKind') != 'movie':
                current['season'] = int(result.get('SeriesSeason'))
                current['episode'] = int(result.get('SeriesEpisode'))

            subtitles.append(current)

        if len(subtitles) > 0:
            if ('season' and 'episode') in subtitles[0].keys():
                pass
            if 'season' in subtitles[0].keys() and 'episode' in subtitles[0].keys():
                subtitles = sorted(
                    subtitles,
                    key=lambda key: (key['season'], key['episode'])
                )

        return {} if data == [] else {
            'available_langs': available_langs,
            'subtitles': subtitles
        }

    def _media_result(self, result: dict, media_type: 'movie' or 'tv') -> Dict[str, str or None] or None:
        '''
        Private helper method to return only required
        data from response fetched using TMDB's API. 
        '''
        poster_path = result.get('poster_path')
        backdrop_path = result.get('backdrop_path')

        # p and b are acronyms of their parent variables
        poster = p if (p := poster_path) is None else f'{self.img_url}/{p}'
        banner = b if (b := backdrop_path) is None else f'{self.img_url}/{b}'

        current: Dict[str, str or None] = {
            'title': result.get('title') or result.get('name'),
            'poster': poster,
            'banner': banner,
            'imdb_id': self._get_imdb_id(result.get('id'), media_type),
            'release_date': None if (rd := result.get('release_date', result.get('first_air_date'))) in self.empty else rd
        }
        return None if current.get('imdb_id') is None else current

    def _get_imdb_id(self, tmdb_id: str, media_type: 'movie' or 'tv') -> str:
        response: dict = requests.get(
            f'{self.base_url}/{media_type}/{tmdb_id}?{self.api_key}&append_to_response=external_ids'
        ).json()

        if media_type == 'movie':
            return _id if (_id := response.get('imdb_id')) not in self.empty else None
        else:
            return _id if (_id := response.get('external_ids').get('imdb_id')) not in self.empty else None


tmdb = TMDB(os.getenv('TMDB_KEY'))
