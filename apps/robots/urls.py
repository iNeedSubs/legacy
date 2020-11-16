from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import RobotsTxt


app_name = 'robots'

urlpatterns = [
    path('robots.txt', RobotsTxt.as_view(), name='txt')
]
