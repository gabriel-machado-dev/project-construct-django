from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

"""
Herda de AbstractUser e adicionar um campo de escolha de cargo.

Para adicionar um campo de escolha de cargo, é necessário criar uma tupla com as opções de escolha e adicionar um campo de escolha de cargo no modelo de usuário.

Para que funcione, é necessário criar um arquivo forms.py no diretório usuarios:

from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = UserChangeForm.Meta.fields

        
class UserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = UserCreationForm.Meta.fields



ROLEPERMISSIONS_MODULE = 'construct_youtube.roles' # diretório pai + arquivo roles

"""

class Users(AbstractUser):
    choice_cargo = [
        ('V', 'Vendedor'),
        ('G', 'Gerente')
    ]
    cargo = models.CharField(max_length=1, choices=choice_cargo)