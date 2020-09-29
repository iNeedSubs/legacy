import requests
from typing import List


class OpenSubs(object):

    base_url = 'https://www.opensubtitles.com/api/v1'
    subtitles_url = 'https://rest.opensubtitles.org/search'

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

        login_credentials = {
            'username': self.username,
            'password': self.password
        }

        response: dict = requests.post(
            f'{self.base_url}/login',
            data=login_credentials
        ).json()

        self.token = response.get('token')
        self.headers = {'Authorization': self.token}
        self.subtitles_headers = {'User-Agent': 'TemporaryUserAgent'}

    def get_media(self, query: str, query_type: 'movie' or 'tv' = 'movie') -> List[dict]:

        response: dict = requests.get(
            f'{self.base_url}/search/{query_type}?query={query}',
            headers=self.headers
        ).json()

        data: List[dict] = response.get('data')
        return [self.media_result(result) for result in data]

    def get_subtitles(self, imdb_id: str, language: str = 'eng') -> List[dict]:

        data: List[dict] = requests.get(
            f'{self.subtitles_url}/imdbid-{imdb_id}/sublanguageid-{language}',
            headers=self.subtitles_headers
        ).json()
        return [self.sub_result(result, result.get('MovieKind')) for result in data]

    def media_result(self, result: dict) -> dict:
        attributes: dict = result.get('attributes')
        current = {
            'title': attributes.get('title'),
            'key_visual': attributes.get('img_url'),
            'imdb_id': str(attributes.get('imdb_id')),
            'release_year': attributes.get('year')
        }
        return current

    def sub_result(self, result: dict, query_type: str) -> dict:
        current = {
            'name': result.get('SubFileName'),
            'language': result.get('SubLanguageID'),
            'download_url': result.get('SubDownloadLink')
        }
        if query_type != 'movie':
            current['episode'] = int(result.get('SeriesEpisode'))
        return current
