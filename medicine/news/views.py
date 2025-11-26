from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NewsArticle
from .forms import NewsArticleForm


class CreateNewsArticleView(LoginRequiredMixin, CreateView):
    model = NewsArticle
    form_class = NewsArticleForm
    template_name = 'news/newsarticle_form.html'
    success_url = reverse_lazy('pages:homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsArticleView(LoginRequiredMixin, UpdateView):
    model = NewsArticle
    form_class = NewsArticleForm
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
    paginate_by = 6


class NewsArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = NewsArticle
    template_name = 'news/newsarticle_confirm_delete.html'
    success_url = reverse_lazy('pages:homepage')
