from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # Login site.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout site.
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),

    # Registration site.
    path('register/', views.register, name='register'),
]
