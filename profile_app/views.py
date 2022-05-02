from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileCreationForm


def profile_page(request, user_id):
    target_user = get_object_or_404(User, username=user_id)
    context = {
        'target_user': target_user
    }
    return render(request, 'profile_app/profile.html', context)


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('profile:profile')

