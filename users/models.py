from django.db import models
from foodfinds.storage_backends import MediaStorage
# Create your models here.

class FoodImages(models.Model):
    food_img = models.FileField(storage=MediaStorage(),upload_to='foods/')