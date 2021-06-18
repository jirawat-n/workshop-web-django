from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=90, required=True, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Confirm Password'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Lastname'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Firstname'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Lastname'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control  textfield-radius col-md-8', 'placeholder': 'Email'})
