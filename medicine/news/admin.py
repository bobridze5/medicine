from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'image')
    search_fields = ('title', 'content', 'author__email')
    list_filter = ('published_date',)
    ordering = ('-published_date',)
