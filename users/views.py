from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import UserResisterForm


# def register_page(request):
#     form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'users/backup/register.html', context)

def register_page(request):
    if request.method == "POST":
        return

    else:
        form = UserResisterForm()
        context = {
            'form': form
        }
    return render(request, 'users/register.html', context)


def profile_page(request):
    return render(request, 'users/profile.html')
