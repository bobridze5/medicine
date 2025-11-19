from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path(
        'create/',
        views.CreateNewsArticleView.as_view(),
        name='create_news_article'
    ),
    path(
        '<int:pk>/',
        views.NewsArticleDetailView.as_view(),
        name='news_article_detail'
    ),
    path('',
         views.NewsArticleListView.as_view(),
         name='news_article_list'
         ),
    path(
        '<int:pk>/delete/',
        views.NewsArticleDeleteView.as_view(),
        name='news_article_delete'
    ),
]
