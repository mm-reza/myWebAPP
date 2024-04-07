# CD to  project
```bash
cd little-lemon-api
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.11.8
pipenv shell
```

## Install Django & frameworks
```bash
# Django
pipenv install django

# Frameworks
pipenv install djangorestframework
pipenv install django-debug-toolbar
# pipenv install djangorestframework-xml
pipenv install bleach
pipenv install djoser
# pipenv install djangorestframework-simplejwt
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

# API endpoints
## Account required
```bash
Admin
    admin
    adminuser123$%^

Delivery crew
    johndoe
    johndoeuser123$%^

Manager
    janedoe
    janedoeuser123$%^

Customer
    babydoe
    babydoeuser123$%^
```
// Tailing / is very important, please check tailing / for rounts.
```bash
POST /auth/users/ for registration send json username and passsword in the body
POST /auth/token/login/
GET /auth/users
GET /auth/users/me/
```

## Menu-items
```bash
GET /api/menu-items
GET /api/menu-items/<int:pk>
```

## User group management 
```bash
GET /api/groups/manager/users
GET /api/groups/manager/users/<int:pk>
```

```bash
GET /api/groups/delivery-crew/users
GET /api/groups/delivery-crew/users/<int:pk>
```

## Cart management
```bash
GET /api/cart/menu-items
```

## Order management
```bash
GET /api/orders
GET/PATCH /api/orders/<int:pk>
```

## Deactivate virtual environment
```bash
exit
```
