# 🌟 User Service 🌟

A **Django REST Framework**-based microservice for **user registration** and **authentication**.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Tests Passed](https://img.shields.io/badge/tests-passed-brightgreen)](https://pytest.org/)

---

## 🚀 Features

- **User Registration** (`POST /signup`)
- **User Login** (`POST /login/`)
- Passwords securely hashed using `bcrypt`
- Clean architecture (separated serializers, views, models)
- Custom User model support
- Environment variable-based configuration
- Postgres database connection setup
- **CORS support** (optional, using `django-cors-headers`)

---

### Prerequisites

- Python 3.13
- PostgreSQL 14+

## ⚙️ Installation

### Clone the Repository

```bash
git clone <your-repo-url>
cd user_service
```

### Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
Create a requirement file add below

# Core
django==5.0.6
djangorestframework==3.15.1

# Database
psycopg[binary]==3.2.6

# Environment
python-dotenv==1.0.1

# Security
bcrypt==4.1.2
PyJWT==2.8.0

# CORS (if needed)
django-cors-headers==4.3.1

# Testing
pytest==8.1.1
pytest-django==4.7.0
factory-boy==3.3.0
```

```bash
pip install -r requirements.txt
```

### Configure Environment

#### Create .env

```bash
DB_NAME=userservice
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key-here
DEBUG=True
```

#### activate .env

```bash
source .env
```

## 🛠️ Setup Instructions

### Database Configuration (PostgreSQL)

#### Create Database and User

```bash
sudo -u postgres psql
CREATE DATABASE userservice;
CREATE USER django_user WITH PASSWORD 'securepassword123';
ALTER ROLE django_user SET client_encoding TO 'utf8';
ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE userservice TO django_user;
\q
```

### Verify Connection

```bash
psql -h localhost -U django_user -d userservice
```

### Django Migrations

##### Apply Initial Migrations

```bash
Add a migration folder in root

python manage.py makemigrations
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

### Run Test

```bash
(to root folder)

pytest
```

### 🏗️ Project Structure

```bash
user_service/
├── tests/                   # Created tests directory
│   └── test_views.py
├── settings/               # Project configuration
│   ├── config.py           # Main settings file
│   ├── urls.py             # Root URL router
│   └── wsgi.py             # WSGI application
│
├── users/                  # Auth app
│   ├── migrations/         # Database migrations
│   ├── models.py           # Custom User model
│   ├── serializers.py      # Request/response serializers
│   ├── views.py            # API view classes
│   ├── urls.py             # App URL routes
│   └── tests/              # Unit tests
│
├── requirements.txt        # Python dependencies
├── manage.py               # Django CLI
└── README.md               # This file
```

## 🚀 Happy Coding!
