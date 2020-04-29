from django import forms

from .models import Post


from django.forms import ModelForm
from .models import Name

from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class NameForm(ModelForm):

    class Meta:
        model = Name
        fields = ('name',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
