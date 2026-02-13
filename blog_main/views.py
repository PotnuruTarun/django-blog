
from django.shortcuts import render,redirect
from blog_main.forms import RegistrationForm
from blogs.models import Category, Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    categories = Category.objects.all()

    featured_posts = Blog.objects.filter(is_featured = True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured= False, status = 'Published').order_by('updated_at')
    context = {
        'categories':categories,
        'featured_posts': featured_posts,
        'posts':posts
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:    
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')