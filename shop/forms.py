from django import forms
from .models import ArticleModel


class ArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel

        fields = [
            'image',
            'name',
            'stock',
            'price',
        ]
