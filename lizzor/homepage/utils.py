from django.db.models import Count
from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # slider новости
        context['slider_posts'] = Article.objects.all().order_by('-pk')[:2]
        # cat_selected по category_slug
        if 'category_slug' in context:
            context['cat_selected'] = Category.objects.get(slug=self.kwargs['category_slug'])
        # Все категории для вывода в header
        context['categories'] = Category.objects.all()
        # Все субкатегории для выбранной категории для вывода в subheader
        if context['cat_selected'] != None:
            context['subcategories'] = Subcategory.objects.filter(parent_category_id=context['cat_selected'].pk)
        # title для страницы
        if 'cat_selected' not in context:
            context['title'] = 'Главная страница'
        else:
            context['title'] = context['cat_selected'].name + ' - Lizzor'
        # меняем title если перешли по субкатегории
        if 'subcat_selected' in context:
            context['title'] = Subcategory.objects.get(slug=context['subcat_selected'].slug).name + ' - Lizzor'
        return context