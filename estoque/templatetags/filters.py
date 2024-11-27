from django import template
from estoque.models import Imagem


"""
O Django possui um sistema de templates que permite a criação de filtros personalizados. Um filtro é uma função que recebe um valor e retorna outro valor.

Para criar um filtro personalizado, você deve criar um arquivo chamado filters.py dentro da pasta templatetags do seu app. Se a pasta templatetags não existir, você deve criá-la.

Dentro do arquivo filters.py, você deve importar a classe template do módulo django e criar um objeto register da classe template.Library.

Em seguida, você deve criar uma função que será o filtro. A função deve receber um valor e retornar outro valor. Para indicar que a função é um filtro, você deve decorá-la com o método filter do objeto register.

Por fim, você deve registrar o filtro no template que deseja usar. Para isso, você deve carregar o arquivo filters.py no template e usar o filtro com o nome que você definiu.

No exemplo acima, criamos um filtro chamado get_first_image que recebe um produto e retorna a URL da primeira imagem do produto. Se o produto não tiver nenhuma imagem, o filtro retorna None.

Para usar o filtro no template, você deve carregar o arquivo filters.py no template com a tag {% load filters %} e usar o filtro com a sintaxe {{ produto|get_first_image }}.

Com isso, você pode criar filtros personalizados para formatar os dados de acordo com as suas necessidades.
"""

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(produto):
    imagem = Imagem.objects.filter(produto=produto).first()
    return imagem.imagem.url if imagem else None