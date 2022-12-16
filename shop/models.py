from django.db import models


class ArticleModel(models.Model):
  image = models.CharField(max_length=300)
  name = models.CharField(max_length=200)
  stock = models.IntegerField()
  price = models.IntegerField()
