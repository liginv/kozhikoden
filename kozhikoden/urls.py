"""kozhikoden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static

admin.autodiscover()

from homepage.views import home
from movies.views import Movies
from movies import urls as api_movie_url
from restaurents import urls as api_restaurent_url
from culturals import urls as api_cultural_url
from events import urls as api_event_url

urlpatterns = [

    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^movies/$', Movies.as_view()),
    url(r'^api/v1/movie/', include(api_movie_url)),
    url(r'^api/v1/restaurent/', include(api_restaurent_url)),
    url(r'^api/v1/cultural/', include(api_cultural_url)),
    url(r'^api/v1/event/', include(api_event_url)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
