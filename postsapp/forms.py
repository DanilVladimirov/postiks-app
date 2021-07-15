from django import forms
from postsapp.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "link"]
