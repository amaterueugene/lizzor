from .models import *
from lizzor.settings import AUTH_USER_MODEL

class ProfileMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        profile = context['profile']
        # Заголовок страницы
        context['title'] = profile.username + ' (' + profile.first_name + ' ' + profile.last_name + ')'

        return context