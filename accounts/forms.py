from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'phone', 'national_id', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'first_name', 'name': 'first_name', 'placeholder': 'Firstname'})
        self.fields['last_name'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'last_name', 'name': 'last_name', 'placeholder': 'Lastname'})
        self.fields['email'].widget.attrs.update(
            {'type': 'email', 'class': 'span12', 'id': 'email', 'name': 'email', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'username', 'name': 'username', 'placeholder': 'Username'})
        self.fields['phone'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'phone', 'name': 'phone', 'placeholder': 'Phone'})
        self.fields['national_id'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'national_id', 'name': 'national_id', 'placeholder': 'National '
                                                                                                           'ID No.'})
        self.fields['password1'].widget.attrs.update(
            {'type': 'password', 'class': 'span12', 'id': 'password1', 'name': 'password1', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'type': 'password', 'class': 'span12', 'password2': 'password2', 'name': 'Password2',
             'placeholder': 'Confirm Password'})



