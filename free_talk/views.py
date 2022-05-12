from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .forms import PostForm
from .models import Post, Comment


def board(request):
    # Input parameter
    # If there's no 'page' parameter input, page value will be 1 as default
    page = request.GET.get('page', 1)

    # Get all post object
    # Order : newer post first
    post_list = Post.objects.order_by('-create_date')

    # Paginator
    per_page = 15
    paginator = Paginator(post_list, per_page)
    page_obj = paginator.get_page(page)

    # Get max page index
    max_index = len(paginator.page_range)

    context = {
        'post_page_obj': page_obj,
        'max_index': max_index,
    }
    return render(request, 'free_talk/board.html', context)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'free_talk/detail.html'


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'target_post'
    form_class = PostForm
    template_name = 'free_talk/update.html'

    def get_success_url(self):
        context = {
            'pk': self.object.pk
        }
        return reverse('free_talk:detail', kwargs=context)


# Discarded
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'free_talk/board.html'
    paginate_by = 8
