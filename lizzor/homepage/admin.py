from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Author)

