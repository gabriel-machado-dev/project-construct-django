from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as auth_admin_django
from .forms import UserChangeForm, UserCreationForm

# Register your models here.

"""
Usamos o decorador @admin.register para registrar o modelo de usuário personalizado.

Substituímos o UserAdmin padrão pelo UserAdmin personalizado.

Adicionamos o campo de escolha de cargo ao UserAdmin personalizado.

form = UserChangeForm: Substituímos o formulário de alteração de usuário padrão pelo formulário de alteração de usuário personalizado.

add_form = UserCreationForm: Substituímos o formulário de criação de usuário padrão pelo formulário de criação de usuário personalizado.

model = Users: Substituímos o modelo de usuário padrão pelo modelo de usuário personalizado.

fieldsets = auth_admin_django.UserAdmin.fieldsets + (('Cargo', {'fields': ('cargo',)}),): Adicionamos o campo de escolha de cargo ao UserAdmin personalizado.

E adicionar o seguinte código no settings.py:

AUTH_USER_MODEL = 'usuarios.Users'

Para adicionar ao banco de dados, execute o seguinte comando:

python manage.py makemigrations
python manage.py migrate
"""

@admin.register(Users)
class UsersAdmin(auth_admin_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = auth_admin_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'cargo'),
        }),
    )
