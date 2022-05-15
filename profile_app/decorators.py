from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = User.objects.get(username=kwargs['user_username']).profile
        if not target_profile == request.user.profile:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
