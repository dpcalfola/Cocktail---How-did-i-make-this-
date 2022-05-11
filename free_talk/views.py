from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment


def board(request):
    return render(request, 'free_talk/board.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'free_talk/board.html'
    paginate_by = 8

