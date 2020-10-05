from django.contrib.auth.models import User
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'