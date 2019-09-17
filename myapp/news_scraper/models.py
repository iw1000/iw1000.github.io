from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Keyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
