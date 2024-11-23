from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

"""

O sinal post_save é emitido sempre que um modelo é salvo. Neste caso, o sinal post_save é emitido sempre que um usuário é salvo.

O decorador @receiver é um receptor de sinal. Ele recebe um sinal e executa uma função.

Neste caso, o receptor de sinal é o sinal post_save e a função é a função assign_role.

A função assign_role é responsável por atribuir uma permissão ao usuário.

Sempre que cria um signals, tem que importar no app.py
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
