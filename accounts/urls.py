from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup_shops/',views.signup_shops,name='signup_shops'),
    path('signup_users/',views.signup_shops,name='signup_users'),
    path('login_shops/',views.login_shops,name='login_shops'),
    path('login_users/',views.login_users,name='login_users'),
    path('logout/',views.logout,name='logout')
]