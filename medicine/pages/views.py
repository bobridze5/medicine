from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import NewsArticle


class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["news_list"] = NewsArticle.objects.all()
        context["news_list"] = NewsArticle.objects.order_by(
            '-published_date')[:6]
        return context
