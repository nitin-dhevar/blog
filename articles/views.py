from django.views.generic import ListView, DetailView 
from . models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html' 

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'