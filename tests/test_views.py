import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

# Create the API client to make requests
@pytest.fixture
def client():
    return APIClient()

# Create a test user
@pytest.fixture
def create_user():
    user = get_user_model().objects.create_user(email='testuser@example.com', password='password123')
    return user

# Test registration endpoint
@pytest.mark.django_db
def test_register(client):
    # Data for the new user registration
    data = {
        "email": "newuser@example.com",
        "password": "password123"
    }
    
    response = client.post('/api/v1/user/signup', data, format='json')

    # Assert that the response status code is 201 (Created)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['message'] == "User registered successfully"

# Test login endpoint (successful login)
@pytest.mark.django_db
def test_login_success(client, create_user):
    # Data for login
    data = {
        "email": create_user.email,
        "password": "password123"
    }

    response = client.post('/api/v1/user/login', data, format='json')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == "Authenticated successfully"

# Test login endpoint (invalid credentials)
@pytest.mark.django_db
def test_login_failure(client, create_user):
    # Data with wrong password
    data = {
        "email": create_user.email,
        "password": "wrongpassword"
    }

    response = client.post('/api/v1/user/login', data, format='json')

    # Assert that the response status code is 401 (Unauthorized)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['error'] == "Invalid credentials"
