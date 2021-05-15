from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.conf import settings 
from django.core.mail import send_mail
from .admin import UserCreationForm
from .models import *

def mail_send(subject,message,email_from,recipient_list):
    send_mail( subject, message, email_from, recipient_list)

def home(request):
    return render(request,'accounts/index.html')

def signup_shops(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_obj = user_form.save(commit=False)
            user_obj.full_name = request.POST['fname']
            user_obj.contact_number = request.POST['contact_number']
            user_obj.user_type = 'ShopOwners'
            user_obj.save()
            mail_send('FoodFinds','Signed Up Successfully',settings.EMAIL_HOST_USER,[user_obj.email, ])
            return redirect('login_shops')
        else:
            return HttpResponse('Not Valid')
    else:
        user_form = UserCreationForm()
        return render(request,'accounts/signup_shops.html',{'user_form':user_form})

def signup_users(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_obj = user_form.save(commit=False)
            user_obj.full_name = request.POST['fname']
            user_obj.contact_number = request.POST['contact_number']
            user_obj.user_type = 'NormalUsers'
            user_obj.save()
            mail_send('FoodFinds','Signed Up Successfully',settings.EMAIL_HOST_USER,[user_obj.email, ])
            return redirect('login_users')
        else:
            return HttpResponse('Not Valid')
    else:
        user_form = UserCreationForm()
        return render(request,'accounts/signup_users.html',{'user_form':user_form})

def login_shops(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user,backend=None)
            return redirect('shops_dashboard')
        else:
            return HttpResponse('Not Valid')
    else:
        return render(request,'accounts/login_shops.html')

def login_users(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user,backend=None)
            return redirect('food_analysis_suggestion')
        else:
            return HttpResponse('Not Valid')
    else:
        return render(request,'accounts/login_users.html')

def logout(request):
    auth.logout(request)
    return redirect('home')