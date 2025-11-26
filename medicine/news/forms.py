from django import forms
from .models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'image']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 10,
                                             'cols': 60,
                                             'placeholder': 'Введите содержание новости здесь...',
                                             'style': 'resize:none;'
                                             }),
        }
