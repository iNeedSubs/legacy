from django.urls import path
from django.conf.urls import url
from .views import Search, SearchMedia, SearchSubtitles


app_name = 'search_v1'

urlpatterns = [
    url(r'^search(/)?$', Search.as_view(), name='search'),
    url(r'^search/show(/)?$', SearchMedia.as_view(), name='show'),
    url(r'^search/movie(/)?$', SearchMedia.as_view(), name='movie'),
    url(r'^search/subtitles(/)?$', SearchSubtitles.as_view(), name='subtitles')
]
