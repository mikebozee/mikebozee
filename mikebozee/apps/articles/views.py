from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Article


def article_list(request):
	articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'articles/list.html', {'articles': articles})


def article_detail(request, slug):
	article = get_object_or_404(Article, slug=slug)
	return render(request, 'articles/detail.html', {'article': article})
