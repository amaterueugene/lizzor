from django.urls import path
from .views import ProfileView, RegisterProfile, LoginProfile, logout_profile

urlpatterns = [
    path('login', LoginProfile.as_view(), name='Login'),
    path('logout', logout_profile, name='Logout'),
    path('register', RegisterProfile.as_view(), name='Register'),
    path('<slug:username>', ProfileView.as_view(), name='ProfilePage'),
]