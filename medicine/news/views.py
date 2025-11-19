from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .models import NewsArticle


class CreateNewsArticleView(CreateView):
    model = NewsArticle
    fields = ['title', 'content', 'author', 'image']
    template_name = 'news/newsarticle_form.html'
    success_url = reverse_lazy('pages:homepage')


class UpdateNewsArticleView(CreateView):
    model = NewsArticle
    fields = ['title', 'content', 'author', 'image']
    template_name = 'news/newsarticle_form.html'
    success_url = reverse_lazy('pages:homepage')


class NewsArticleDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/newsarticle_detail.html'
    context_object_name = 'news_article'


class NewsArticleListView(ListView):
    model = NewsArticle
    template_name = 'news/newsarticle_list.html'
    context_object_name = 'news_list'
    paginate_by = 10


class NewsArticleDeleteView(DeleteView):
    model = NewsArticle
    template_name = 'news/newsarticle_confirm_delete.html'
    success_url = reverse_lazy('pages:homepage')
