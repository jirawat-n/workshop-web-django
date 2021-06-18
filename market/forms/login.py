from django import forms


class loginforms(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control textfield-radius input-sm'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control textfield-radius input-sm', 'type': 'password'}))
