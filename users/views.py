from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.conf import settings 
from django.contrib.auth.decorators import login_required
import requests
from shops.models import *
from accounts.models import *
from .models import *

@login_required
def food_analysis_suggestion(request):
    if request.method == 'POST':
        product = request.POST['product']
        url = 'https://api.spoonacular.com/recipes/complexSearch?query='+str(product)+'&apiKey=5a9e06330e8146da874b12c8dde75226'
        searched_product = requests.get(url).json()['results'][0]
        url = 'https://api.spoonacular.com/recipes/guessNutrition?title='+str(product)+'&apiKey=5a9e06330e8146da874b12c8dde75226'
        nutrition_response = requests.get(url).json()
        maxcal = str(nutrition_response['calories']['confidenceRange95Percent']['max'])
        mincal = str(nutrition_response['calories']['confidenceRange95Percent']['min'])
        maxfat = str(nutrition_response['fat']['confidenceRange95Percent']['max'])
        minfat = str(nutrition_response['fat']['confidenceRange95Percent']['min'])
        maxcarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['max'])
        mincarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['min'])
        maxprot = str(nutrition_response['protein']['confidenceRange95Percent']['max'])
        minprot = str(nutrition_response['protein']['confidenceRange95Percent']['min'])
        url = 'https://api.spoonacular.com/recipes/findByNutrients?apiKey=5a9e06330e8146da874b12c8dde75226&minCarbs='+mincarbs+'&maxCarbs='+maxcarbs+'&maxCalories='+maxcal+'&minCalories='+mincal+'&maxProtein='+maxprot+'&minProtein='+minprot+'&maxFat='+maxfat+'&minFat='+minfat+'&number=10'
        suggested_by_nutrients = requests.get(url).json()
        url = 'https://api.spoonacular.com/recipes/'+str(searched_product['id'])+'/similar?apiKey=5a9e06330e8146da874b12c8dde75226'
        similar_foods = requests.get(url).json()
        context = {
            'product':product,
            'searched_product':searched_product,
            'suggested_by_nutrients':suggested_by_nutrients,
            'similar_foods':similar_foods
        }
        return render(request,'users/food_analysis_suggestion_results.html',context)
    else:
        return render(request,'users/food_analysis_suggestion.html')

@login_required
def food_analysis_suggestion_by_image(request):
    if request.method == 'POST':
        img = FoodImages(food_img=request.FILES['food'])
        img.save()
        url = 'https://api.spoonacular.com/food/images/classify?imageUrl=https://foodfinds.blob.core.windows.net/media/' + str(img.food_img) +'&apiKey=5a9e06330e8146da874b12c8dde75226'
        searched_product = requests.get(url).json()['category']
        url = 'https://api.spoonacular.com/recipes/guessNutrition?title='+str(searched_product)+'&apiKey=5a9e06330e8146da874b12c8dde75226'
        nutrition_response = requests.get(url).json()
        maxcal = str(nutrition_response['calories']['confidenceRange95Percent']['max'])
        mincal = str(nutrition_response['calories']['confidenceRange95Percent']['min'])
        maxfat = str(nutrition_response['fat']['confidenceRange95Percent']['max'])
        minfat = str(nutrition_response['fat']['confidenceRange95Percent']['min'])
        maxcarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['max'])
        mincarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['min'])
        maxprot = str(nutrition_response['protein']['confidenceRange95Percent']['max'])
        minprot = str(nutrition_response['protein']['confidenceRange95Percent']['min'])
        url = 'https://api.spoonacular.com/recipes/findByNutrients?apiKey=5a9e06330e8146da874b12c8dde75226&minCarbs='+mincarbs+'&maxCarbs='+maxcarbs+'&maxCalories='+maxcal+'&minCalories='+mincal+'&maxProtein='+maxprot+'&minProtein='+minprot+'&maxFat='+maxfat+'&minFat='+minfat+'&number=10'
        suggested_by_nutrients = requests.get(url).json()
        url = 'https://api.spoonacular.com/recipes/complexSearch?query=' + str(searched_product) + '&apiKey=5a9e06330e8146da874b12c8dde75226'
        foodid = requests.get(url).json()['results'][0]['id']
        url = 'https://api.spoonacular.com/recipes/'+str(foodid)+'/similar?apiKey=5a9e06330e8146da874b12c8dde75226'
        similar_foods = requests.get(url).json()
        context = {
            'searched_product':searched_product,
            'suggested_by_nutrients':suggested_by_nutrients,
            'similar_foods':similar_foods
        }
        return render(request,'users/food_analysis_suggestion_by_img_results.html',context)
    else:
        return HttpResponse('Invalid Request')

@login_required
def shops(request):
    if request.method == 'POST':
        product = request.POST['product']
        url = 'https://api.spoonacular.com/recipes/complexSearch?query='+str(product)+'&apiKey=5a9e06330e8146da874b12c8dde75226'
        searched_product = requests.get(url).json()['results'][0]
        url = 'https://api.spoonacular.com/recipes/guessNutrition?title='+str(product)+'&apiKey=5a9e06330e8146da874b12c8dde75226'
        nutrition_response = requests.get(url).json()
        maxcal = str(nutrition_response['calories']['confidenceRange95Percent']['max'])
        mincal = str(nutrition_response['calories']['confidenceRange95Percent']['min'])
        maxfat = str(nutrition_response['fat']['confidenceRange95Percent']['max'])
        minfat = str(nutrition_response['fat']['confidenceRange95Percent']['min'])
        maxcarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['max'])
        mincarbs = str(nutrition_response['carbs']['confidenceRange95Percent']['min'])
        maxprot = str(nutrition_response['protein']['confidenceRange95Percent']['max'])
        minprot = str(nutrition_response['protein']['confidenceRange95Percent']['min'])
        url = 'https://api.spoonacular.com/recipes/findByNutrients?apiKey=5a9e06330e8146da874b12c8dde75226&minCarbs='+mincarbs+'&maxCarbs='+maxcarbs+'&maxCalories='+maxcal+'&minCalories='+mincal+'&maxProtein='+maxprot+'&minProtein='+minprot+'&maxFat='+maxfat+'&minFat='+minfat+'&number=10'
        suggested_by_nutrients = requests.get(url).json()
        url = 'https://api.spoonacular.com/recipes/'+str(searched_product['id'])+'/similar?apiKey=5a9e06330e8146da874b12c8dde75226'
        similar_foods = requests.get(url).json()
        inventory_products = list()
        prods = Inventory_Products.objects.filter(product_name=str(product).lower()).all()
        for prod in prods:
            inventory_products.append(prod)
        for food in suggested_by_nutrients:
            products = Inventory_Products.objects.filter(product_name=str(food['title']).lower()).all()
            if len(products) != 0:
                for product in products:
                    inventory_products.append(product)
        for food in similar_foods:
            products = Inventory_Products.objects.filter(product_name=str(food['title']).lower()).all()
            if len(products) != 0:
                for product in products:
                    inventory_products.append(product)
        return render(request,'users/shops_result.html',{'inventory_products':inventory_products})
    else:
        return render(request,'users/shop_search.html')

@login_required
def addCart(request,pk):
    product = Inventory_Products.objects.filter(pk=pk).first()
    Orders(requested_from=request.user,requested_to=product.profile,product=product,status='Ordered').save()
    return redirect('cart')

@login_required
def cart(request):
    orders = Orders.objects.filter(requested_from=request.user).all()
    return render(request,'users/orders.html',{'orders':orders})

@login_required
def meal_plan(request):
    if request.method == 'POST':
        url = 'https://api.spoonacular.com/mealplanner/generate?apiKey=5a9e06330e8146da874b12c8dde75226&timeFrame=day&targetCalories='+str(request.POST['number'])
        response = requests.get(url).json()['meals']
        return render(request,'users/showmealplan.html',{'response':response})
    else:
        return render(request,'users/mealplan.html')