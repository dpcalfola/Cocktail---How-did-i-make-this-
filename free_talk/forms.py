from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content_text', 'content_image']

        labels = {
            'subject': '제목',
            'content_text': '내용',
        }
