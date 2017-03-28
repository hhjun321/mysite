# coding: utf-8
from django.conf.urls import  url
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^out/$', views.out, name='out'),
       
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

