from .models import Category,Blog

def get_categories(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    return dict(categories = categories , blogs= blogs)