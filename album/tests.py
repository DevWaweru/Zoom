from django.test import TestCase
from .models import Location, Category, Image
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.nairobi = Location(photo_location='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def tearDown(self):
        self.nairobi.delete_location()
    
    def test_updating_location(self):
        self.nairobi.update_location(self.nairobi.id, 'Kitengela')
        self.assertTrue(self.nairobi.photo_location != 'Kitengela')
    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.sports = Category(photo_category='Sports')
        self.sports.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))
    
    def tearDown(self):
        self.sports.delete_category()
    
    def test_updating_category(self):
        self.sports.update_category(self.sports.id, 'Utility')
        self.assertTrue(self.sports.photo_category != 'Utility')
    
