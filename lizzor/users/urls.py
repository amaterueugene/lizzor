from django.urls import path
from .views import *

urlpatterns = [
    path('login', ProfileView.as_view(), name='Login'),
    path('register', RegisterProfile.as_view(), name='Register'),
    path('<slug:username>', ProfileView.as_view(), name='ProfilePage'),
]