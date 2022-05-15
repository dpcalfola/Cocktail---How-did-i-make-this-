from django.http import HttpResponseForbidden

from free_talk.models import Post


def post_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # CBV로 넘어오는 <int:pk> 값을 **kwargs 를 이용하여 dictionary 형태로 가져올 수 있음
        author = Post.objects.get(pk=kwargs['pk']).author
        if not author == request.user.profile:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
