from django.shortcuts import render

from .forms import UserResisterForm


def profile_page(request):
    return render(request, 'users/profile.html')


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

# Replaced this CBV to FBV but don't forget how to work this way
# class AccountCreateView(CreateView):
#     model = User
#     form_class = UserResisterForm
#     success_url = reverse_lazy('users:create_done')
#     template_name = 'users/create.html'


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
