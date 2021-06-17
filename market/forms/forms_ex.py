from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from market.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

