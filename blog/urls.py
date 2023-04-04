from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import blog, criarpost, create_Post, blog_post

urlpatterns = [
    path('', blog, name='index'),
    path('criarpost', criarpost, name="criarpost"),
    path('create_Post', create_Post, name='create_Post'),
    path('blog_post/<int:id>', blog_post, name='blog_post')


]
