import os
import requests
from typing import List, Dict


class TMDB(object):
    '''
    Class to wrap TMDB API endpoints into methods for ease of use.
    '''
    img_url = 'https://image.tmdb.org/t/p/original'
    base_url = 'https://api.themoviedb.org/3/search'
    id_lookup_url = 'https://api.themoviedb.org/3'

    def __init__(self, api_key: str) -> None:
        self.api_key = f'api_key={api_key}'

    def get_movie(self, query: str) -> List[dict]:
        '''
        Returns a list of movies with given query from TMDB API.
        '''
        response: dict = requests.get(
            f'{self.base_url}/movie?query={query}&{self.api_key}'
        ).json()
        results: List[str] = list(response.get('results'))
        return [self._media_result(result, 'movie') for result in results]

    def get_show(self, query: str):
        '''
        Returns a list of movies with given query from TMDB API.
        '''
        response: dict = requests.get(
            f'{self.base_url}/tv?query={query}&{self.api_key}'
        ).json()
        results = response.get('results')
        return [self._media_result(result, 'tv') for result in results]

    def get_media(self, query: str, media_type='movie' or 'tv'):
        return self.get_movie(query) if media_type == 'movie' else self.get_show(query)

    def get_media_from_id(self, imdb_id):
        pass

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
            'release_date': None if (rd := result.get('release_date')) in [None, ''] else rd
        }
        return None if current.get('imdb_id') is None else current

    def _get_imdb_id(self, tmdb_id: str, media_type: 'movie' or 'tv') -> str:
        response: dict = requests.get(
            f'{self.id_lookup_url}/{media_type}/{tmdb_id}?{self.api_key}&append_to_response=external_ids'
        ).json()

        if media_type == 'movie':
            return response.get('imdb_id')
        else:
            return response.get('external_ids').get('imdb_id')


def _sub_result(result: dict) -> dict:
    '''
    Helper function for get_subtitles() to set properties needed only.
    This is a private function and use should be avoided anywhere else.
    '''
    current = {
        'name': result.get('SubFileName'),
        'language': result.get('SubLanguageID'),
        'download_url': result.get('SubDownloadLink')
    }
    if result.get('MovieKind') != 'movie':
        current['episode'] = int(result.get('SeriesEpisode'))
    return current


def get_subtitles(imdb_id: str, language: str = 'eng', media=None) -> List[dict]:
    subtitles_url = 'https://rest.opensubtitles.org/search'
    headers = {'User-Agent': 'TemporaryUserAgent'}

    data: List[dict] = requests.get(
        f'{subtitles_url}/imdbid-{imdb_id}/sublanguageid-{language}',
        headers=headers
    ).json()

    return [_sub_result(result) for result in data]


tmdb = TMDB(os.getenv('TMDB_KEY'))
