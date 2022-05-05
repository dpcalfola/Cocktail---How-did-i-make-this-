from django.shortcuts import render

from .forms import UserResisterForm
from profile_app.models import Profile


def account_create(request):
    if request.method == 'POST':
        user_form = UserResisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            context = {
                'new_user_id': new_user.username
            }
            return render(request, 'users/login.html', context)
    else:
        user_form = UserResisterForm()

    context = {
        'form': user_form,
    }
    return render(request, 'users/signup.html', context)
