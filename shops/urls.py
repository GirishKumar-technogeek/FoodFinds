from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='shops_dashboard'),
    path('addProfile/',views.addProfile,name='addProfile'),
    path('inventory/',views.inventory,name='shops_inventory'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('deleteProduct/<int:pk>',views.deleteProduct,name='deleteProduct'),
    path('orders/',views.orders,name='orders'),
    path('substitute_products/',views.substitute_products,name='substitute_products')
]