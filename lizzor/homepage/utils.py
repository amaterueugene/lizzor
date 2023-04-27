from django.db.models import Count
from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()
        if context['cat_selected'] != None:
            context['subcategories'] = Subcategory.objects.filter(parent_category_id=context['cat_selected'].pk)
        return context