# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from main import views
from tts.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^polis/', include('polis.urls', namespace='polis')),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^tts/', tts_play),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
