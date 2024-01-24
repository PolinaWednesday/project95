from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, logout_view, RegisterView, ProfileView, generate_new_password, confirm_registration, \
    invalid_token_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('confirm-registration/<str:token>/', confirm_registration, name='confirm_registration'),
    path('invalid-token/', invalid_token_view, name='invalid_token'),
]