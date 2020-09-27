from django.urls import path
from .views import SearchEndpoint


app_name = 'middleman'

urlpatterns = [
    path('search/', SearchEndpoint.as_view(), name='search'),
]
