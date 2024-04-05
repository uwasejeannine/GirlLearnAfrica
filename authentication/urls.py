from django.urls import path
from authentication.views import signup, user_login

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', user_login, name='login'),
]