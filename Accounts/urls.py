from django.urls import path
from .views import register_user, user_login, test_token, get_all_users, Home, register_page, Endpoints

urlpatterns = [
    path('', Home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('test_token/', test_token, name='test_token'),
    path('users/', get_all_users, name='get_all_users'),
    path('register-form/', register_page, name='register_page'),
    path('apiendpoints/', Endpoints, name='endpoints'),
    
]