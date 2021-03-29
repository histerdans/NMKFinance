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
            {'type': 'text', 'class': 'span12', 'id': 'Firstname', 'name': 'Firstname', 'placeholder': 'Firstname'})
        self.fields['last_name'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'Lastname', 'name': 'Lastname', 'placeholder': 'Lastname'})
        self.fields['email'].widget.attrs.update(
            {'type': 'email', 'class': 'span12', 'id': 'Email', 'name': 'Email', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'Username', 'name': 'Username', 'placeholder': 'Username'})
        self.fields['phone'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'Phone', 'name': 'Phone', 'placeholder': 'Phone'})
        self.fields['national_id'].widget.attrs.update(
            {'type': 'text', 'class': 'span12', 'id': 'idno', 'name': 'idno', 'placeholder': 'National ID No.'})
        self.fields['password1'].widget.attrs.update(
            {'type': 'password', 'class': 'span12', 'id': 'Password1', 'name': 'Password1', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'type': 'password', 'class': 'span12', 'id': 'Password2', 'name': 'Password2',
             'placeholder': 'Confirm Password'})



