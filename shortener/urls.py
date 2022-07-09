from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shortener'
urlpatterns = [
    path('', views.main_view),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('new_short/', views.short_view, name='new_short/'),
    path('myshorts/', views.myshorts_view, name='myshorts/'),
]
