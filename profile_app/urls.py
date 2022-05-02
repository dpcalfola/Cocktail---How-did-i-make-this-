from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<user_id>/', views.profile_page, name='profile'),
]
