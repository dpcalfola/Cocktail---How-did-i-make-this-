from django.urls import path
from . import views

app_name = 'free_talk'

urlpatterns = [
    path('', views.board, name='board'),
]
