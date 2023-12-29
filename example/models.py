from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True) # 책 id
    title = models.CharField(max_length=50) # book title
    author = models.CharField(max_length=50) # author
    category = models.CharField(max_length=50) # category
    pages = models.IntegerField() # pages
    price = models.IntegerField() # price
    published_date = models.DateField() # published_date
    description = models.TextField() # description