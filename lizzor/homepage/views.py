from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Subcategory, Article
from .utils import DataMixin


class ShowArticlesView(DataMixin, ListView):
    model = Article
    template_name = 'homepage/index.html'
    context_object_name = 'articles'

    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(cat_selected=Category.objects.get(slug='business'))
        return dict(list(context.items())+list(c_def.items()))
    

class ShowCatArticlesView(DataMixin, ListView):
    model = Article
    template_name = 'homepage/index.html'
    context_object_name = 'articles'

    paginate_by = 7


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(cat_selected=Category.objects.get(slug=self.kwargs['category_slug']))
        return dict(list(context.items())+list(c_def.items()))
    

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'])
    

class ShowSubCatArticlesView(DataMixin, ListView):
    model = Article
    template_name = 'homepage/index.html'
    context_object_name = 'articles'

    paginate_by = 7


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=Category.objects.get(slug=self.kwargs['category_slug']))
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug']).filter(subcategory__slug=self.kwargs['subcategory_slug'])
