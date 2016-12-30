# coding: utf-8
from django.conf.urls import  url
from photo import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #photo 출력    
    url(r'^photo/(?P<photo_id>\d+)$',views.single_photo, name='view_single_photo'),
    
    #photo upload
    url(r'^photo/upload/$',views.new_photo, name='new_photo'),
    
    url(r'^out/$', views.out, name='out'),   
    url(r'^cam/$', views.open, name='cam'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

