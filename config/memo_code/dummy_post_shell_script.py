from free_talk.models import Post
from profile_app.models import Profile
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

writer = get_object_or_404(Profile, user_id=1)

for i in range(300):
    post = Post(subject=f'Post 더미 데이터: {i:3d}', content_text='내용 무', author=user)
    post.save()

