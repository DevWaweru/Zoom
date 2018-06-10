from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    photo_location = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.photo_location

class Category(models.Model):
    photo_category = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update

    def __str__(self):
        return self.photo_category

class Image(models.Model):
    image = models.ImageField(upload_to = 'museum-Images/',default='Image')
    name = models.CharField(max_length=30)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    catergory = models.ForeignKey(Category)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image
    
    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(category__icontains=search_category)
        return images_category

    @classmethod
    def filter_by_location(cls, filter_location):
        images_location = Image.objects.filter(location__photo_location=filter_location)
        return images_location   