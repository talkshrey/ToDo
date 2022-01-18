from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import TaskList
from django.contrib.auth.forms import UserCreationForm

class TaskCreate(forms.ModelForm):
    class Meta:
        model = TaskList
        fields =  ['title', 'description', 'compulsory', 'priority_order']

class CreateUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'image']