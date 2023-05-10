from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterProfileForm
from .models import Profile
from .utils import ProfileMixin

class ProfileView(ProfileMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(profile=context['profile'])
        return dict(list(context.items())+list(c_def.items()))


class RegisterProfile(CreateView):
    form_class = RegisterProfileForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('HomePage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    

class LoginProfile(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self):
        return reverse_lazy('HomePage')