from django import forms
from django.contrib.auth.models import User


class login_form(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('email','password')
class singup_form (forms.ModelForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    username =forms.CharField()
    email =forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')
