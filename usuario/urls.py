from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import login, register

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
]
