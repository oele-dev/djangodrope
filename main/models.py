from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)
    publish_at = models.DateTimeField("date published")