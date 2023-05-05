from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:username>', ProfileView.as_view(), name='ProfilePage' )
]