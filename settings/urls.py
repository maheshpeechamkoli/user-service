"""
User service URL Configuration
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [
    # Health check endpoint
    re_path(settings.API_PREFIX + "health-check", lambda r: HttpResponse()),
    
    # Users API endpoints
    path(settings.API_PREFIX + '', include('users.urls')),
]