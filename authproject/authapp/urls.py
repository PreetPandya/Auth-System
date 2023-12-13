from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.signpage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.homepage, name='home'),
    path('logout/', views.logoutpage, name='logout')
]
