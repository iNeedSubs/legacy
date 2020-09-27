import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


EXTERNAL_BASE_URL = 'https://rest.opensubtitles.org'


class SearchEndpoint(GenericAPIView):

    def get(self, *args, **kwargs):
        return Response(self.get_queryset())

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        language = self.request.query_params.get('language', None)

        if query is None:
            return {'err': 'Provide a search query.'}

        external_api = f'{EXTERNAL_BASE_URL}/search/query-{query}/sublanguageid-{language}'
        headers = {
            'User-Agent': 'TemporaryUserAgent'
        }

        response = requests.get(external_api, headers=headers)
        return response.json()
