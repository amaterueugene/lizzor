from django.views.generic import DetailView
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
