from unicodedata import category
from django.db import models
from distutils.command.upload import upload
import datetime as dt
from cloudinary.models import CloudinaryField 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

   #method for updating category
    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id=id).update(name = name)

    
    def __str__(self):
        return self.name

    

class Location(models.Model):
    name = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def update_location(self, name):
        self.name = name
        self.save()

    def __str__(self):
        return self.name

   


class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        image_id = cls.objects.filter(id = id).all()
        return image_id

    @classmethod
    def filter_by_location(cls,location):
        image_location = cls.objects.filter(location__name=location).all()
        return image_location
    
    @classmethod
    def filter_by_category(cls,category):
        images = cls.objects.filter(category__name=category).all()
        return images

    @classmethod
    def update_image(cls,id,name,description,location,category):
        update = cls.objects.filter(id = id).update(name = name, description = description, location = location, category = category)
        return update

    def __str__(self):
        return self.name

   







