import os

from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tresh', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название статьи'
            }
        )

        self.fields['tresh'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Содержимое'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Добавьте изображение'
            }
        )

