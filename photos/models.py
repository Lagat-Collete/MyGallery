from django.db import models
from distutils.command.upload import upload
import datetime as dt

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to =' ')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    posted_date = models.DateTimeField(auto_now_add=True)





