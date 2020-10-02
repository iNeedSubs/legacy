from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.core.models import open_subs


class Search(GenericAPIView):

    def get(self, *args, **kwargs):
        return Response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        media_type: str = self.request.query_params.get('type', 'movie')
        return_type: str = self.request.query_params.get('return', 'media')
        language: str = self.request.query_params.get('lang', 'eng')

        if query is None:
            return [{'err': 'Provide a search query.'}]

        if media_type not in ['tv', 'movie']:
            return [{'err': 'Unknown media type provided: movie or tv'}]

        media = open_subs.get_media(query, media_type)

        if return_type.lower() == 'media':
            return media
        elif return_type.lower() == 'subtitles':
            return open_subs.get_subtitles(media[0].get('imdb_id'), language) if len(media) > 0 else []
        else:
            return [{'err': 'Unknown return type provided: media or subtitles.'}]


class SearchMedia(GenericAPIView):

    def get(self, *args, **kwargs):
        return Response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        if query is None:
            return [{'err': 'Provide a search query.'}]

        if self.request.path == reverse('search_v1:search_movie'):
            return open_subs.get_media(query)
        else:
            return open_subs.get_media(query, 'tv')


class SearchSubtitles(GenericAPIView):

    def get(self, *args, **kwargs):
        return Response(self.get_queryset())

    def get_queryset(self):
        imdb_id: str or None = self.request.query_params.get('imdb_id')
        language: str = self.request.query_params.get('lang', None)

        if imdb_id is None:
            return [{'err': 'Provide the imdb_id of a movie/show.'}]

        return open_subs.get_subtitles(imdb_id, language)
