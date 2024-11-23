from django import forms
from .models import Users
from django.contrib.auth import forms

"""
Essas classes são necessárias para que o Django possa criar um formulário de criação de usuário e um formulário de alteração de usuário.

Herdamos das classes mas alteramos a classe Meta para que o Django possa criar os formulários com os campos do modelo de usuário.
colocando model = Users e 
          fields = UserChangeForm.Meta.fields e UserCreationForm.Meta.fields.
"""

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users
        fields = forms.UserChangeForm.Meta.fields
       

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        fields = forms.UserCreationForm.Meta.fields
        
        