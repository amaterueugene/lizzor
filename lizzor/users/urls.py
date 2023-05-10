from django.urls import path
from .views import ProfileView, RegisterProfile, LoginProfile

urlpatterns = [
    path('login', LoginProfile.as_view(), name='Login'),
    path('register', RegisterProfile.as_view(), name='Register'),
    path('<slug:username>', ProfileView.as_view(), name='ProfilePage'),
]