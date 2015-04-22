from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'NBA/$', views.nba, name='NBA'),
	url(r'NHL/$', views.nhl, name='NHL'),
	url(r'NFL/$', views.nfl, name='NFL'),
	url(r'(?P<ID>[0-9])/$', views.detail, name='detail'),
]