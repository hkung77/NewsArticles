from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader



from .models import article
# Create your views here.


def index(request):
	article_list = article.objects.order_by('-Pub_date')
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
		'article_list':article_list,
	})
	return HttpResponse(template.render(context))
		
def nba(request):
	article_list = article.objects.order_by('-Pub_date').filter(Category='NBA')
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
	'article_list':article_list,
	})
	return HttpResponse(template.render(context))

def nfl(request):
	article_list = article.objects.order_by('-Pub_date').filter(Category='NFL')
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
	'article_list':article_list,
	})
	return HttpResponse(template.render(context))

def nhl(request):
	article_list = article.objects.order_by('-Pub_date').filter(Category='NHL')
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
	'article_list':article_list,
	})
	return HttpResponse(template.render(context))
	
def detail(request,ID="0"):
	article_id = article.objects.get(id=ID)
	
	template = loader.get_template('article/detail.html')
	context = RequestContext(request, {
	'article_id':article_id,
	})
	return HttpResponse(template.render(context))
