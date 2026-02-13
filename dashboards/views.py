from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404

from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm,BlogForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blogs_count': blogs_count
    }
    return render(request,'dashboard.html', context)

def categories(request):
    return render(request,'categories_ds.html')

def add_category(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form' : form
    }
    return render(request, 'add_category.html', context)

def edit_category(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    category = get_object_or_404(Category, id = id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'edit_category.html', {'form': form})

def delete_category(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')








def all_posts(request):
    posts = Blog.objects.filter(status = 'Published')
    context = {
        'posts': posts
    }
    return render(request, 'all_posts.html', context)


def add_post(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = BlogForm()
    context = {
        'form' : form
    }
    return render(request, 'add_posts.html', context)

def edit_post(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    post = get_object_or_404(Blog, id = id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = BlogForm(instance=post)

    return render(request, 'edit_posts.html', {'form': form})

def delete_post(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to perform this action.")
    post = get_object_or_404(Blog, id=id)
    post.delete()
    return redirect('all_posts')



