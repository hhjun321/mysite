# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polis/', include('polis.urls', namespace='polis')),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^main/', include('main.urls', namespace='main')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
