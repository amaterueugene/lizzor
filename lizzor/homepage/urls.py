from django.urls import path, include
from django.conf.urls.static import static
from .views import ShowArticlesView, ShowCatArticlesView, ShowSubCatArticlesView
from lizzor import settings


urlpatterns = [
    path('', ShowArticlesView.as_view(), name='HomePage'),
    path('category/<slug:category_slug>', ShowCatArticlesView.as_view(), name='CategoryPage'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>', ShowSubCatArticlesView.as_view(), name='SubCategoryPage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

