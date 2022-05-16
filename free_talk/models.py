from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from profile_app.models import Profile

# Load snippet
from snippets.image_logic import compress_image


# # For image compression
# from io import BytesIO
# from PIL import Image
# from django.core.files import File
#
#
# # Image compression method
# def compress_image(image):
#     temp_image = Image.open(image).convert('RGB')
#     temp_image_io = BytesIO()
#     temp_image.save(temp_image_io, 'jpeg', quality=80)
#     new_image = File(temp_image_io, name=image.name)
#     return new_image


class Post(models.Model):
    subject = models.CharField(max_length=200)
    content_text = models.TextField()
    content_image = models.ImageField(upload_to='free_talk/image/', null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # Override .save
    def save(self, *args, **kwargs):
        new_content_image = compress_image(self.content_image)
        self.content_image = new_content_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_text = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.subject
