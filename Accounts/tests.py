from django.test import TestCase

# Create your tests here.

POST http://localhost:8000/api/login/
Content-Type: application/json

{"username": "admin1", "password": "admin2"}

###

POST http://localhost:8000/api/register/
Content-Type: application/json

{"username": "admin1", "password": "admin2", "email":"hassa@gmail.com", "last_name":"yange", "first_name": "hassan", "phone": "0764977815"}

###

GET http://localhost:8000/api/test_token/
Content-Type: application/json

Authorization: Token fea9504231f205b677a0ae0aaa518a52ae2e554d