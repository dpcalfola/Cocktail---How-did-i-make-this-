from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<user_username>/', views.profile_page, name='profile'),
    path('update/<user_username>/', views.profile_update, name='update')
]
