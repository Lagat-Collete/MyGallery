from unicodedata import category
from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category= Category(name= 'trees')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

    def test_update_category(self):
        self.category.save_category()
        self.category.update_category(self.category.id, "Trees")
        changed_category = Category.objects.filter(name ='Trees')
        self.assertTrue(len(changed_category)>0)


class ImageTestClass(TestCase):
    
    def setUp(self):
        self.image=Image(name='solomon', description='one of the smaller islands in Oceania', location = 'Location', category='self.category',posted_date ='28-05-2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image =Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, "Hummingbird.jpg")
        changed_image = Image.objects.filter(name ='Hummingbird.jpg')
        self.assertTrue(len(changed_image) > 0)

        
        


    

      


