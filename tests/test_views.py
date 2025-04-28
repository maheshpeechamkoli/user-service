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
    user = get_user_model().objects.create_user(
        email='testuser@example.com',
        password='password123'
    )
    return user

# Test registration endpoint
@pytest.mark.django_db
def test_register(client):
    data = {
        "email": "newuser@example.com",
        "password": "password123"
    }
    response = client.post('/api/v1/user/signup', data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    # existing message assertion, assuming signup still returns a message
    assert response.data['message'] == "User registered successfully"

# Test login endpoint (successful login)
@pytest.mark.django_db
def test_login_success(client, create_user):
    data = {
        "email": create_user.email,
        "password": "password123"
    }
    response = client.post('/api/v1/user/login', data, format='json')

    assert response.status_code == status.HTTP_200_OK
    # verify returned user fields instead of message
    assert 'id' in response.data
    assert 'email' in response.data
    assert response.data['id'] == create_user.id
    assert response.data['email'] == create_user.email

# Test login endpoint (invalid credentials)
@pytest.mark.django_db
def test_login_failure(client, create_user):
    data = {
        "email": create_user.email,
        "password": "wrongpassword"
    }
    response = client.post('/api/v1/user/login', data, format='json')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['error'] == "Invalid credentials"
