from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

# Create your models here.

"""
O relacionamento será de 1 para muitos, ou seja, uma categoria pode ter vários produtos, mas um produto só pode ter uma categoria.

Para isso, usamos o campo ForeignKey, que é um campo que faz referência a outro modelo. No caso, o campo categoria do modelo Produto faz referência ao modelo Categoria.

O parâmetro on_delete=models.SET_NULL indica que, caso a categoria seja deletada, o campo categoria do produto será setado como NULL.

O parâmetro null=True indica que o campo categoria pode ser NULL, ou seja, um produto pode não ter uma categoria associada.

O método __str__ é um método especial que retorna uma representação em string do objeto. Nesse caso, ele retorna o nome do produto, mas você pode alterar para retornar o que quiser.

Em um site comercial, os campos que mexem com dinheiro devem ser do tipo BinaryField para evitar problemas com arredondamento de valores. O campo quantidade também é do tipo BinaryField para evitar problemas com arredondamento de valores.

slug é um campo que será usado para gerar uma URL amigável para o produto. Ele é do tipo SlugField, que é um campo que aceita apenas letras, números, hífens e underlines. O parâmetro unique=True indica que o campo deve ser único, ou seja, não pode haver dois produtos com o mesmo slug. O parâmetro blank=True indica que o campo pode ser vazio, e o parâmetro null=True indica que o campo pode ser NULL.



"""

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo
    

class Produto(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # SET_NULL: se a categoria for deletada, o produto não será deletado e a categoria do produto será setada como NULL
    quantidade = models.FloatField()
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)
   
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)
    
    def gerar_desconto(self, desconto):
        return self.preco_venda - (self.preco_venda * (desconto / 100))
        
    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return  (lucro * 100) / self.preco_compra

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagem_produto/')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) # CASCADE: se o produto for deletado, a imagem também será deletada

