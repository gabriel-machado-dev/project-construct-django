from rolepermissions.roles import AbstractUserRole

"""
Atraves dessa classe, é possível criar as permissões de cada usuário
Grupos de usuários, irá ter um vendendor, um gerente e um administrador...

available_permissions é um dicionário que contém as permissões que cada usuário terá
"""


class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True,
    }

"""
Para o Django roles.py não existe, por isso é necessário em settings.py adicionar a seguinte linha:

ROLEPERMISSIONS_MODULE = 'construct_youtube.roles' # diretório pai + arquivo roles
"""