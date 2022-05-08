from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<user_username>/', views.profile_page, name='profile'),
    path('update_page/<user_username>/', views.profile_update_page, name='update_page'),
    path('update/<user_username>/', views.profile_update, name='update'),
]
