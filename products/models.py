from django.db import models

class Product(models.Model):
  title = models.CharField()
  url = models.CharField()
  pub_date = models.DateTimeField()
  votes_total = models.IntegerField()
  image = models.ImageField()