from django.forms import ModelForm
from django import forms
from .models import UserLogin

class UserForm(ModelForm):
    class Meta:
        model = UserLogin
        fields = "__all__"
    