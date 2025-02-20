from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=64)


class News(models.Model):
    headline = models.CharField(max_length=128)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
