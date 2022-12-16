from django.contrib import admin
from .models import ArticleModel

class ArticleAdmin(admin.ModelAdmin):
    fields = ['image', 'name', 'stock', 'price']

admin.site.register(ArticleModel)