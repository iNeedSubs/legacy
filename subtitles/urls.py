"""subtitles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from subtitles.views import VueView


urlpatterns = [
    path('', include('apps.robots.urls')),
    path('admin', RedirectView.as_view(url='admin/')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.v1.search.urls')),
    path('sitemap.xml',
         TemplateView.as_view(
             template_name='sitemap.xml',
             content_type='text/xml'
         )
         ),
    url(r'^.*', VueView.as_view(), name='app')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
