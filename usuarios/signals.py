from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

"""

O SINAL POST_SAVE É EMITIDO SEMPRE QUE UM MODELO É SALVO. NESTE CASO, O SINAL POST_SAVE É EMITIDO SEMPRE QUE UM USUÁRIO É SALVO.

O DECORADOR @RECEIVER É UM RECEPTOR DE SINAL. ELE RECEBE UM SINAL E EXECUTA UMA FUNÇÃO.

NESTE CASO, O RECEPTOR DE SINAL É O SINAL POST_SAVE E A FUNÇÃO É A FUNÇÃO ASSIGN_ROLE.

A FUNÇÃO ASSIGN_ROLE É RESPONSÁVEL POR ATRIBUIR UMA PERMISSÃO AO USUÁRIO.

SEMPRE QUE CRIA UM SIGNALS, TEM QUE IMPORTAR NO APP.PY
"""

@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    """
    sender: qual a classe que foi feita a observação
    instance: instância que foi feita a observação, se foi feita no usuario vou saber as informações do usuario
    created: se foi criado ou não
    **kwargs: argumentos adicionais
    """
    if created:
        if instance.cargo == 'V':
            assign_role(instance, 'vendedor')
        elif instance.cargo == 'G':
            assign_role(instance, 'gerente')
