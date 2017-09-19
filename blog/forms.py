from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta: # where we tell django which model should be used to create form
        model = Post
        fields = ('title', 'text')
        # only need title & text
        # author is currently logged in
        # created_date is automatically set when we create a post
