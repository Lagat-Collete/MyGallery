from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CtegoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wild= Category(name= 'wild')

      


