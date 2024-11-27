from rolepermissions.roles import AbstractUserRole

"""
ATRAVES DESSA CLASSE, É POSSÍVEL CRIAR AS PERMISSÕES DE CADA USUÁRIO
GRUPOS DE USUÁRIOS, IRÁ TER UM VENDEDOR, UM GERENTE E UM ADMINISTRADOR...

AVAILABLE_PERMISSIONS É UM DICIONÁRIO QUE CONTÉM AS PERMISSÕES QUE CADA USUÁRIO TERÁ
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