from django import forms
from .models import ExtendedUser, Wall, Comments


class WallMessageForm(forms.ModelForm):
    class Meta:
        model = Wall
        fields = ['message']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class LoginForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['username', 'password']

    password = forms.CharField(
        max_length=512,
        widget=forms.PasswordInput
    )


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    email = forms.CharField(
        max_length=254,
        widget=forms.EmailInput
    )

    password = forms.CharField(
        max_length=512,
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        max_length=512,
        widget=forms.PasswordInput
    )