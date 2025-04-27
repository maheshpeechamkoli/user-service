"""
Users service URL Configuration
"""
from django.urls import path
from users.views import RegisterView, LoginView

app_name = 'users'

urlpatterns = [
    path('signup', RegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
]