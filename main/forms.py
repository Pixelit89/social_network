from django import forms
from .models import ExtendedUser, Wall, Comments


class WallMessageForm(forms.ModelForm):
    class Meta:
        model = 'Wall'
        fields = ['message']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = 'Comments'
        fields = ['comment']