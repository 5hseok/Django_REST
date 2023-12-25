from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    price = models.IntegerField()