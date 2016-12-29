from django.conf.urls import  url
from polis import views


urlpatterns = [
    # /polis/
    url(r'^$', views.index, name='index'),

    # /plis/5
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),

    # /plis/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),

    # /plis/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

	url(r'^out/$', views.out, name='out'),
	
	
    url(r'^cam/$', views.open, name='cam'),

]

