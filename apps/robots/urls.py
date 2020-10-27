from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import RobotsTxt


app_name = 'robots'

urlpatterns = [
    path('robots.txt/', RedirectView.as_view(url=reverse_lazy('robots:txt')), name='alias'),
    path('robots.txt', RobotsTxt.as_view(), name='txt')
]
