from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

"""
has_permission_decorator() é um decorador que verifica se o usuário tem permissão para acessar a view.
Ex: apenas o gerente pode cadastrar vendedores

em roles.py, foi criado a permissão 'cadastrar_vendedor' e foi atribuido a classe Gerente
"""

@has_permission_decorator(permission_name='cadastrar_vendedor') # 
def cadastrar_vendedor(request):
    if request.method == 'GET':
        vendedores = Users.objects.filter(cargo='V')
        return render(request, 'cadastrar_vendedor.html', {'vendedores': vendedores})
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            validate_email(email)
        except ValidationError:
            messages.add_message(request, messages.ERROR, 'Email inválido')
            return redirect(reverse('cadastrar_vendedor'))
            

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do django
            messages.add_message(request, messages.ERROR, 'Email já cadastrado')
            return redirect(reverse('cadastrar_vendedor'))
        
        user = Users.objects.create_user(username=email, email=email, password=senha, first_name=nome, last_name=sobrenome, cargo='V')

        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Vendedor cadastrado com sucesso')
    

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=login, password=senha)

        if not user:
            # TODO: Redirecionar com uma mensagem de erro
            return HttpResponse('Usuário não encontrado')
        auth_login(request, user)
        return HttpResponse('Logado com sucesso')
    

def logout(request):
    request.session.flush() # Limpa a sessão do usuário
    return redirect(reverse('login')) # Redireciona para a página de login

@has_permission_decorator(permission_name='cadastrar_vendedor')
def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id) # buscar a info na tabela Users pelo id\
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluído com sucesso')
    return redirect(reverse('cadastrar_vendedor')) # Redireciona para a página de cadastro de vendedores