from django.shortcuts import render, redirect
from .models import Product, Categories
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def category(request, foo):
    foo = foo.replace('-',' ')
    # grab the category from the url

    try:
        # look up the category
        category = Categories.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    
    except:
        messages.success(request, ("That category Doesn't exist..."))
        return redirect('home')    

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        
        else:
             messages.success(request, ("There is an error, please"))
        return redirect('login')
    else:
        return render(request, 'login.html', {})

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out... Thank you'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()                         # We define the form
    if request.method == 'POST':                # Checking if theyre filling the form
        form = SignUpForm(request.POST)         # Our filled form that we'll use to authenticate them
        if form.is_valid:                          
            form.save()                         
            username = form.cleaned_data['username'] # We use the filled out info to log our users in
            password = form.cleaned_data['password1']

            # login the user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered successfully"))
            return redirect('home')
        else:
            messages.success(request, ('There was a problem registering '))
    else:    
        return render(request, 'register.html', {'form':form})
    