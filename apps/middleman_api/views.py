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
            return {'err': 'Provide a search query.'}

        external_api = f'{EXTERNAL_BASE_URL}/search/query-{query}/sublanguageid-{language}'
        response = requests.get(external_api, headers=HEADERS)
        results: List[dict] = response.json()

        final: List[dict] = []

        for result in results:
            if result.get('MovieKind') not in ['tv series', 'episode']:
                if result.get('MovieKind') == query_type.lower():
                    current = self.set_result(result)

            current = self.set_result(result)

            final.append(current)

        return final

    def set_result(self, result) -> dict:
        current = {
            'title': result.get('MovieReleaseName'),
            'name': result.get('SubFileName'),
            'language': result.get('SubLanguageID'),
            'downloadUrl': result.get('SubDownloadLink')
        }
        return current
