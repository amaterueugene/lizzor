from django.urls import path, include
from django.conf.urls.static import static
from .views import ShowArticlesView
from lizzor import settings


urlpatterns = [
    path('', ShowArticlesView.as_view(), name='HomePage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

