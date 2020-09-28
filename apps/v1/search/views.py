import requests
from typing import List
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


EXTERNAL_BASE_URL = 'https://rest.opensubtitles.org'
HEADERS = {
    'User-Agent': 'TemporaryUserAgent'
}


class SearchEndpoint(GenericAPIView):

    def get(self, *args, **kwargs):
        return Response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query', None)
        language: str = self.request.query_params.get('language', 'eng')
        query_type: str = self.request.query_params.get('type', 'movie')

        if query is None:
            return [{'err': 'Provide a search query.'}]

        external_api = f'{EXTERNAL_BASE_URL}/search/query-{query}/sublanguageid-{language}'
        response = requests.get(external_api, headers=HEADERS)
        results: List[dict] = response.json()

        final: List[dict] = []
        show_list = ['episode', 'tv series']

        for result in results:
            if query_type.lower() in show_list:
                if result.get('MovieKind') in show_list:
                    final.append(self.set_result(result))
            else:
                if result.get('MovieKind') == query_type.lower():
                    final.append(self.set_result(result))

        return final

    def set_result(self, result) -> dict:
        current = {
            'title': result.get('MovieReleaseName'),
            'name': result.get('SubFileName'),
            'language': result.get('SubLanguageID'),
            'downloadUrl': result.get('SubDownloadLink')
        }
        return current
