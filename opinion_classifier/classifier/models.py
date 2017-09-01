from django.db import models

class Article(models.Model):
    """
    Model for a New York Times article
    """
    url = models.CharField(max_length=250)
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length=250)
    text = models.TextField()
    type = models.CharField(max_length=100)
