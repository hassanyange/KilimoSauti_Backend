from django.urls import path
from .views import register_user, user_login, test_token

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('test_token/', test_token, name='test_token')
]