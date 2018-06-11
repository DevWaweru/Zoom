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