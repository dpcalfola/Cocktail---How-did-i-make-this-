from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_image/', null=True)
    wallpaper = models.ImageField(upload_to='profile_wallpaper/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    introduce = models.CharField(max_length=150, null=True)
