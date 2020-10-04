from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import tmdb, get_subtitles


def _get_response(queryset) -> Response:
    status_code = 200

    if isinstance(queryset, dict):
        status_code = status_code if 'detail' not in queryset else 400

    return Response(queryset, status=status_code)


class Search(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        media_type: str = self.request.query_params.get('type', 'movie')
        return_type: str = self.request.query_params.get('return', 'media')
        language: str = self.request.query_params.get('lang', 'eng')

        if query is None:
            return {'detail': 'Provide a search query.'}

        if media_type not in ['tv', 'movie']:
            return {'detail': 'Unknown media type provided: movie or tv'}

        media = tmdb.get_media(query, media_type.lower())

        if return_type.lower() == 'media':
            return media
        elif return_type.lower() == 'subtitles':
            return get_subtitles(media[0].get('imdb_id'), language) if len(media) > 0 else []
        else:
            return {'detail': 'Unknown return type provided: media or subtitles.'}


class SearchMedia(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        if query is None:
            return {'detail': 'Provide a search query.'}

        if self.request.path == reverse('search_v1:search_movie'):
            return tmdb.get_movie(query)
        else:
            return tmdb.get_show(query)


class SearchSubtitles(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        imdb_id: str or None = self.request.query_params.get('imdb_id')
        language: str = self.request.query_params.get('lang', 'eng')

        if imdb_id is None:
            return {'detail': 'Provide the imdb_id of a movie/show.'}

        return get_subtitles(tmdb, imdb_id, language)
