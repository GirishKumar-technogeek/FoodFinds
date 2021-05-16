from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.conf import settings 
from django.contrib.auth.decorators import login_required
import requests
from .models import *
from accounts.models import *

@login_required
def dashboard(request):
    profile = ShopOwnerProfile.objects.filter(user=request.user).first()
    if profile is None:
        return redirect('addProfile')
    return render(request,'shops/profile.html',{'profile':profile})

@login_required
def addProfile(request):
    if request.method == 'POST':
        ShopOwnerProfile(user=request.user,shop_name=request.POST['shop_name'],shop_description=request.POST['shop_description'],shop_location=request.POST['shop_location']).save()
        return redirect('shops_dashboard')
    else:
        return render(request,'shops/addprofile.html')

@login_required
def inventory(request):
    profile = ShopOwnerProfile.objects.filter(user=request.user).first()
    products = Inventory_Products.objects.filter(profile=profile).all()
    return render(request,'shops/inventory.html',{'products':products})

@login_required
def addProduct(request):
    if request.method == 'POST':
        profile = ShopOwnerProfile.objects.filter(user=request.user).first()
        product = Inventory_Products(profile=profile,product_name=str(request.POST['product_name']).lower(),price=request.POST['price'])
        url = 'https://api.spoonacular.com/recipes/guessNutrition?title='+str(product.product_name)+'&apiKey=APIKEY'
        nutrition_response = requests.get(url).json()
        product.calories = round(float(nutrition_response['calories']['value']),2)
        product.max_calories = round(float(nutrition_response['calories']['confidenceRange95Percent']['max']),2)
        product.min_calories = round(float(nutrition_response['calories']['confidenceRange95Percent']['min']),2)
        product.carbs = round(float(nutrition_response['carbs']['value']),2)
        product.max_carbs = round(float(nutrition_response['carbs']['confidenceRange95Percent']['max']),2)
        product.min_carbs = round(float(nutrition_response['carbs']['confidenceRange95Percent']['min']),2)
        product.fat = round(float(nutrition_response['fat']['value']),2)
        product.max_fat = round(float(nutrition_response['fat']['confidenceRange95Percent']['max']),2)
        product.min_fat = round(float(nutrition_response['fat']['confidenceRange95Percent']['min']),2)
        product.protein = round(float(nutrition_response['protein']['value']),2)
        product.max_protein = round(float(nutrition_response['protein']['confidenceRange95Percent']['max']),2)
        product.min_protein = round(float(nutrition_response['protein']['confidenceRange95Percent']['min']),2)
        product.save()
        return redirect('shops_inventory')
    else:
        return render(request,'shops/addproduct.html')

@login_required
def deleteProduct(request,pk):
    profile = ShopOwnerProfile.objects.filter(user=request.user).first()
    Inventory_Products.objects.filter(profile=profile,pk=pk).delete()
    return redirect('shops_inventory')

@login_required
def orders(request):
    profile = ShopOwnerProfile.objects.filter(user=request.user).first()
    orders = Orders.objects.filter(requested_to=profile).all()
    return render(request,'shops/orders.html',{'orders':orders})

@login_required
def substitute_products(request):
    product = request.POST['product']
    url = 'https://api.spoonacular.com/recipes/complexSearch?query='+str(product)+'&apiKey=APIKEY'
    searched_product = requests.get(url).json()['results'][0]
    url = 'https://api.spoonacular.com/recipes/guessNutrition?title='+str(product)+'&apiKey=APIKEY'
    nutrition_response = requests.get(url).json()
    maxcal = str(nutrition_response['calories']['confidenceRange95Percent']['max'])
    mincal = str(nutrition_response['calories']['confidenceRange95Percent']['min'])
    maxfat = str(nutrition_response['fat']['confidenceRange95Percent']['max'])
    minfat = str(nutrition_response['fat']['confidenceRange95Percent']['min'])
    maxcarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['max'])
    mincarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['min'])
    maxprot = str(nutrition_response['protein']['confidenceRange95Percent']['max'])
    minprot = str(nutrition_response['protein']['confidenceRange95Percent']['min'])
    url = 'https://api.spoonacular.com/recipes/findByNutrients?apiKey=APIKEY&minCarbs='+mincarbs+'&maxCarbs='+maxcarbs+'&maxCalories='+maxcal+'&minCalories='+mincal+'&maxProtein='+maxprot+'&minProtein='+minprot+'&maxFat='+maxfat+'&minFat='+minfat+'&number=10'
    suggested_by_nutrients = requests.get(url).json()
    url = 'https://api.spoonacular.com/recipes/'+str(searched_product['id'])+'/similar?apiKey=APIKEY'
    similar_foods = requests.get(url).json()
    context = {
        'product':product,
        'searched_product':searched_product,
        'suggested_by_nutrients':suggested_by_nutrients,
        'similar_foods':similar_foods
    }
    return render(request,'shops/substitute_products.html',context)
        
