from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from core.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','status','priority']

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
