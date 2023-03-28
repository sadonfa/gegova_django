from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article

# Create your views here.


def list(request):

    article = Article.objects.all()

    paginator = Paginator(article, 3)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': page_articles 
    })


def category(request, id):

    category = get_object_or_404 (Category, pk=id)
    articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, pk=article_id)

    return render(request, 'articles/article.html',{
        'article': article
    })
    