from django.shortcuts import render, redirect
from django.http import request
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have created your account!")
            return redirect('')
        
    context = {'form': form}
    
    return render(request, 'website/register.html', context=context)

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()  
            auth_login(request, user)
            messages.success(request, "You have logged into your account!")
            return redirect('')  
            

    return render(request, 'website/login.html', {"form": form})

def user_logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out!")
    return redirect('')


