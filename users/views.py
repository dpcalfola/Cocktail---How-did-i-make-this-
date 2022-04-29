from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserResisterForm


def profile_page(request):
    return render(request, 'users/profile.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('main:index')
    template_name = 'users/create.html'

# DISCARDED
# register is going to be made in Class based view

# def register_page(request):
#     form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'users/backup/register.html', context)

# def register_page(request):
#     if request.method == "POST":
#         return
#
#     else:
#         form = UserResisterForm()
#         context = {
#             'form': form
#         }
#     return render(request, 'users/register.html', context)
