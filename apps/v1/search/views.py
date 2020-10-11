from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import tmdb


EMPTY = [None, '']


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

        if query in EMPTY:
            return {
                'detail': 'No query has been passed or passed empty string',
                'type': 'NO_QUERY'
            }

        if media_type not in ['tv', 'movie']:
            return {
                'detail': 'Unknown media type provided: movie or tv',
                'type': 'WRONG_MEDIA_TYPE'
            }

        media = tmdb.get_media(query, media_type.lower())

        if return_type.lower() == 'media':
            return media
        elif return_type.lower() == 'subtitles':
            return tmdb.get_subtitles(media[0].get('imdb_id'), language) if len(media) > 0 else []
        else:
            return {
                'detail': 'Unknown return type provided: media or subtitles.',
                'type': 'WRONG_RETURN_TYPE'
            }


class SearchMedia(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        if query in EMPTY:
            return {
                'detail': 'No query has been passed or passed empty string',
                'type': 'NO_QUERY'
            }

        if self.request.path == reverse('search_v1:movie'):
            return tmdb.get_movie(query)
        else:
            return tmdb.get_show(query)


class SearchSubtitles(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        imdb_id: str or None = self.request.query_params.get('imdb_id')
        language: str = self.request.query_params.get('lang', 'eng')

        if imdb_id in EMPTY:
            return {
                'detail': 'No ID has been passed',
                'type': 'NO_ID'
            }

        subtitles = tmdb.get_subtitles(imdb_id, language)

        if not subtitles:
            return {
                'detail': 'Movie with that ID does not exist',
                'type': 'WRONG_ID'
            }

        return tmdb.get_subtitles(imdb_id, language)
