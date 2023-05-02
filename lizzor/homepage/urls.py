from django.urls import path, include
from django.conf.urls.static import static
from .views import ShowArticlesView, ShowCatArticlesView
from lizzor import settings


urlpatterns = [
    path('', ShowArticlesView.as_view(), name='HomePage'),
    path('category/<slug:category_slug>', ShowCatArticlesView.as_view(), name='CategoryPage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

