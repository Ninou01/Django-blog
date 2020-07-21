from django import forms
from ckeditor.fields import RichTextField
from .models import Post , Comment

class CreatePostForm(forms.ModelForm):
    content = RichTextField()
    class Meta:    
        model = Post
        fields = ["title","content","tags","public","img"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class EmailForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

