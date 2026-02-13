
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),


] 