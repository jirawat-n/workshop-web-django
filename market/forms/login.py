from django import forms


class login_boot(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control input-sm','type':'password'}))

