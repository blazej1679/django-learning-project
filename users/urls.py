"""Definiuje wzorce adresow URL dla aplikacji users."""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #Strona logowania.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #Strona wylogowania.
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    #strona rejestracji
    path('register/', views.register, name='register'),
]
