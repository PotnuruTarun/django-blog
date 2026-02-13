
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete_category'),

    path('all_posts' , views.all_posts , name = 'all_posts'),
    path('all_posts/add/', views.add_post, name='add_post'),
    path('all_posts/edit/<int:id>/', views.edit_post, name='edit_post'),
    path('all_posts/delete/<int:id>/', views.delete_post, name='delete_post'),

] 