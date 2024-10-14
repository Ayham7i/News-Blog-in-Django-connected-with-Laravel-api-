from django.shortcuts import render
from .services import ApiService

api_service = ApiService()

def article_list(request):
    articles = api_service.get_articles()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = api_service.get_article(article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
