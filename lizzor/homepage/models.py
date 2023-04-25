from django.db import models


class Author(models.Model):
    '''Автор публикации(не профиль пользователя)'''
    fullname = models.CharField(max_length=255, verbose_name='Имя автора')

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Image(models.Model):
    '''Главное изображение публикации. Также показываемое на карточке публикации'''
    title = models.CharField(max_length=255, verbose_name='Название')
    source = models.CharField(max_length=100, verbose_name='Источник')
    image = models.ImageField(upload_to='images/%Y/%m/', verbose_name="Изображение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



class Category(models.Model):
    '''Родительская категория публикаций широкого профиля'''
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    '''Дочерняя категория узкого профиля'''
    name = models.CharField(max_length=50, verbose_name='Субкатегория')
    parent_category = models.ForeignKey('Category', on_delete=models.PROTECT)
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Субкатегория'
        verbose_name_plural = 'Субкатегории'


class Article(models.Model):
    '''Публикация'''
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    summary = models.CharField(max_length=400, verbose_name='Краткое описание')
    content = models.CharField(verbose_name='Контент')
    image = models.ForeignKey('Image', on_delete=models.PROTECT)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    time_created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0 ,verbose_name='Просмотры')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


