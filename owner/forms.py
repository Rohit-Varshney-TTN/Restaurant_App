from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','confirm_password']
