from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def register_page(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
