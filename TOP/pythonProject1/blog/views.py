from django.shortcuts import render, get_object_or_404

from .models import Article # подключение базы данных
app_name = 'blog'
# Create your views here.
def blogView(request):
    articles = Article.objects.all() # отвечает за хранение подключенной базы
    print(articles[0].desc)
    return render(request, template_name='blog/blog.html', context={'articles':articles})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail/detail.html', {'article':article})
