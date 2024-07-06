from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('blog-detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('comment/create/', views.comment_create, name='comment_create')
]