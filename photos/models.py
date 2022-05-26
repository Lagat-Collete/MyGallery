from django.db import models
from distutils.command.upload import upload
import datetime as dt

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def __str__(self):
        return self.name

    

class Location(models.Model):
    name = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name

   


class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        images = Image.objects.filter(category__icontains=search_term)
        return images



    def __str__(self):
        return self.name

   







