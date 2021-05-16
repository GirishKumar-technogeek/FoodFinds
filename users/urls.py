from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('food_analysis_suggestion/',views.food_analysis_suggestion,name='food_analysis_suggestion'),
    path('food_analysis_suggestion_by_image/',views.food_analysis_suggestion_by_image,name='food_analysis_suggestion_by_image'),
    path('shops/',views.shops,name='shops'),
    path('cart/',views.cart,name='cart'),
    path('addCart/<int:pk>',views.addCart,name='addCart'),
    path('meal_plan/',views.meal_plan,name='meal_plan')
]