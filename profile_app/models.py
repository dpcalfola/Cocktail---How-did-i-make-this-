from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # OneToOneField => User 테이블의 user_id 컬럼을 외래키로 연결짓는 듯?
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    wallpaper = models.ImageField(upload_to='profile_wallpaper/', null=True, blank=True)
    nickname = models.CharField(max_length=30, unique=True, null=True, blank=True)
    introduce = models.CharField(max_length=150, null=True, blank=True)

    @property
    def writer(self):
        if self.nickname:
            return self.nickname
        else:
            temp_writer = '@' + str(self.user.username)
            return temp_writer

    def __str__(self):
        return self.user.username
