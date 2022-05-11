from django.urls import path
from . import views

app_name = 'free_talk'

urlpatterns = [
    # path('', views.PostListView.as_view(), name='board'),
    path('', views.board, name='board')
]
