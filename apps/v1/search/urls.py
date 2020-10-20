from django.urls import path
from .views import Search, GetMedia, GetSubtitles


app_name = 'search_v1'

urlpatterns = [
    path('search', Search.as_view(), name='search'),
    path('media', GetMedia.as_view(), name='media'),
    path('subtitles', GetSubtitles.as_view(), name='subtitles')
]
