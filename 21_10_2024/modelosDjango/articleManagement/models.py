from django.db import models
# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    price = models.IntegerField()
    category = models.CharField(max_length = 30)