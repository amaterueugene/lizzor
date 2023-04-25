from django.urls import path, include
from .views import ShowArticlesView


urlpatterns = [
    path('', ShowArticlesView.as_view(), name='HomePage'),
]