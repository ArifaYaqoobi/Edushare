from django import forms
from .models import Resource, Comment

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'subject', 'grade', 'uploaded_file', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows':2, 'placeholder':'Add a helpful comment...'})
        }
