from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'free_talk/board.html'
    paginate_by = 8


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
