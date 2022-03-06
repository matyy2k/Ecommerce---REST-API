# Ecommerce---REST-API

## Table of Contents

* General info
* Technologies
* How to run


## General info
This is an e-commerce REST API built on the Django REST Framework.  
Contains models of books, products and also allows you to add items to the basket for individual users.  
To do this, you need authorization, which consists in generating a special token.


## Technologies
- Python 3.10
- Django 4.0.2


## How to run

* You can create applications locally on your computer:

1) git clone https://github.com/matyy2k/Ecommerce---REST-API.git
2) pip install -r requirements-dev.txt
3) python manage.py migrate
4) python manage.py runserver  
  
* You can open the website online:
https://ecommerce-restapi-djangoapp.herokuapp.com/

I suggest using 'Postman' application.  

ATTENTION  
The token is required for individual POST requests. The user must be authorized or has access only to the GET methods.  

Available methods:

| Link | GET | POST |
| --- | --- |  --- |
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/users/ | List of users | Add new user (type username and password)
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/auth/ | NOT ALLOWED | Get an individual token
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/categories/ | Category list | Add new category
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/books/ | Books list | Add new book
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/products/ | Products list | Add new product
| https://ecommerce-restapi-djangoapp.herokuapp.com/api/v1/carts/ | Cart | First define books and products







