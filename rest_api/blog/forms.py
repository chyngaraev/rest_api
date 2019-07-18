from django import forms
from .models import Post, PostComments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email addess')



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content', 'image')


    class PostCommentForm(forms.ModelForm):

        class Meta:
            model = PostComments
            fields = ('content_comment', 'image_comment')
