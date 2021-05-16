from django.db import models
# Create your models here.

class FoodImages(models.Model):
    food_img = models.FileField(upload_to='foods/')