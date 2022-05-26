from django.db import models
from distutils.command.upload import upload
import datetime as dt

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to =' ')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    def save_Image(self):
        self.save()







