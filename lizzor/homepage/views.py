from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Subcategory, Article
from .utils import DataMixin


class ShowArticlesView(DataMixin, ListView):
    model = Article
    template_name = 'homepage/index.html'
    context_object_name = 'article'

    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = Category.objects.get(slug='business')
        c_def = self.get_user_context(title='Главная страница', cat_selected=context['cat_selected'])
        return dict(list(context.items())+list(c_def.items()))