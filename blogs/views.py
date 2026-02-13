from django.shortcuts import render,redirect
from .models import Blog, Category
# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status= 'Published', category_id = category_id)
    try:
        category = Category.objects.get(pk = category_id)
    except:
        return render(request, '404.html')
    context = {'posts' :posts,
               'category': category}
    return render(request, 'posts_by_category.html',context)