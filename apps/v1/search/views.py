from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import tmdb
from .langs import languages
from .exceptions import get_status_code


EMPTY = [None, '']


def _get_response(queryset) -> Response:
    status_code = 200

    if isinstance(queryset, dict):
        if 'type' in queryset:
            status_code = get_status_code(queryset['type'])
            if status_code == 500:
                queryset['details'] = 'An internal server error has occurred.'

    return Response(queryset, status=status_code)


class Search(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        query: str or None = self.request.query_params.get('query')
        media_type: str = self.request.query_params.get('type')
        return_type: str = self.request.query_params.get('return', 'media')
        language: str = self.request.query_params.get('lang', 'all')

        if query in EMPTY:
            return {
                'detail': 'No query has been passed or passed empty string',
                'type': 'NO_QUERY'
            }

        if media_type in EMPTY or media_type not in ['show', 'movie']:
            return {
                'detail': 'Type passed does not exist',
                'type': 'INVALID_TYPE'
            }
        media_type = 'tv' if media_type == 'show' else media_type

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


class GetMedia(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        imdb_id: str or None = self.request.query_params.get('imdb_id')

        if imdb_id in EMPTY:
            return {
                'detail': 'No ID has been passed',
                'type': 'NO_ID'
            }

        return tmdb.get_media_from_id(imdb_id)


class GetSubtitles(GenericAPIView):

    def get(self, *args, **kwargs):
        return _get_response(self.get_queryset())

    def get_queryset(self):
        imdb_id: str or None = self.request.query_params.get('imdb_id')
        language: str = self.request.query_params.get('lang')

        if imdb_id in EMPTY:
            return {
                'detail': 'No ID has been passed',
                'type': 'NO_ID'
            }

        if language not in EMPTY:
            if language not in languages:
                return {
                    'detail': 'Unrecognized language code used',
                    'type': 'WRONG_LANG_CODE'
                }
        else:
            language = 'all'

        subtitles = tmdb.get_subtitles(imdb_id, language)

        if not subtitles:
            return {
                'detail': 'Movie with that ID does not exist',
                'type': 'WRONG_ID'
            }

        return subtitles
