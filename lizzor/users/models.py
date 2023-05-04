from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from homepage.models import Article


class Profile(AbstractUser):
    GENDER = (
        ('male', 'Мужчина'), 
	    ('female', 'Женщина'),
    )

    POSITION = (
	    ('writer', 'Автор'), 
	    ('reader', 'Читатель'), 
	    ('editor', 'Редактор'), 
	    ('admin', 'Админ'),
	    ('moderator', 'Модератор'),
    )

    username = models.CharField(max_length=100, unique=True, blank=False, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=100, unique=True, blank=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    birth_date = models.DateField(default='2002-01-01', verbose_name='Дата рождения')
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, verbose_name='Пол')
    country = CountryField(blank=True, verbose_name='Страна')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars/%Y/%m/', blank=True, verbose_name='Аватар')
    password = models.CharField(max_length=50, blank=False, verbose_name='Пароль')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    position = models.CharField(max_length=9, choices=POSITION, default='reader', verbose_name='Роль')
    bookmarks = models.ManyToManyField(Article, blank=True, related_name='bookmarks', verbose_name='Закладки')
    read_later = models.ManyToManyField(Article, blank=True, related_name='read_later', verbose_name='Читать позже')
    history = models.ManyToManyField(Article, blank=True, verbose_name='История')
    
    



