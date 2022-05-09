from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    subject = models.CharField(max_length=200)
    content_text = models.TextField()
    content_image = models.ImageField(upload_to='free_talk/image/', null=True, blank=True)
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_text = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.subject
