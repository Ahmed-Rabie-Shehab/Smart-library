from django.urls import path 
from . import views

urlpatterns = [
    path('login', views.login_page, name="login"),
    path('register', views.register_page, name="register"),
    path('profile', views.profile_page, name="profile"),
]    
