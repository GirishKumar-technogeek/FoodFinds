from django.db import models
from accounts.models import *

class ShopOwnerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    shop_description = models.TextField()
    shop_location = models.TextField()

class Inventory_Products(models.Model):
    profile = models.ForeignKey(ShopOwnerProfile,on_delete=models.CASCADE)
    product_name = models.TextField()
    price = models.CharField(max_length=50)
    calories = models.DecimalField(max_digits=15, decimal_places=3)
    max_calories = models.DecimalField(max_digits=15, decimal_places=3)
    min_calories = models.DecimalField(max_digits=15, decimal_places=3)
    carbs = models.DecimalField(max_digits=15, decimal_places=3)
    max_carbs = models.DecimalField(max_digits=15, decimal_places=3)
    min_carbs = models.DecimalField(max_digits=15, decimal_places=3)
    fat = models.DecimalField(max_digits=15, decimal_places=3)
    max_fat = models.DecimalField(max_digits=15, decimal_places=3)
    min_fat = models.DecimalField(max_digits=15, decimal_places=3)
    protein = models.DecimalField(max_digits=15, decimal_places=3)
    max_protein = models.DecimalField(max_digits=15, decimal_places=3)
    min_protein = models.DecimalField(max_digits=15, decimal_places=3)

class Orders(models.Model):
    requested_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_requested')
    requested_to = models.ForeignKey(ShopOwnerProfile,on_delete=models.CASCADE,related_name='to_requested')
    product = models.TextField()
    status = models.TextField(null=True)