from django.urls import path
from .views import Search, SearchMedia, SearchSubtitles


app_name = 'search_v1'

urlpatterns = [
    path('search', Search.as_view(), name='search'),
    path('subtitles', SearchSubtitles.as_view(), name='subtitles')
]
