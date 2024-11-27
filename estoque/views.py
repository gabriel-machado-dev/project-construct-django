from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ProdutoForm
from .models import Categoria, Produto, Imagem
from datetime import date
from PIL import Image, ImageDraw
from io import BytesIO
from rolepermissions.decorators import has_permission_decorator
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your views here.

@has_permission_decorator('cadastrar_produto')
def add_produto(request):
    if request.method == 'GET':
        nome = request.GET.get('nome')
        categoria = request.GET.get('categoria')
        preco_min = request.GET.get('preco_min')
        preco_max = request.GET.get('preco_max')

        produtos = Produto.objects.all()

        if nome or categoria or preco_min or preco_max:
            if not preco_min:
                preco_min = 0
            if not preco_max:
                preco_max = 999999
            if nome:
                # O método __icontains faz uma busca case-insensitive, ou seja, não diferencia maiúsculas de minúsculas
                produtos = produtos.filter(nome__icontains=nome)
            if categoria:
                produtos = produtos.filter(categoria=categoria)
            # O método filter aceita múltiplos parâmetros, e ele faz uma busca com todos os parâmetros passados
            # __gte: maior ou igual
            # __lte: menor ou igual
            produtos = produtos.filter(preco_venda__gte=preco_min, preco_venda__lte=preco_max)

        categorias = Categoria.objects.all()
        
        return render(request, 'add_produto.html', {'categorias': categorias, 'produtos': produtos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')

        

        produto = Produto(nome=nome, categoria_id=categoria, quantidade=quantidade, preco_compra=preco_compra, preco_venda=preco_venda)
        produto.save()

        imagens = request.FILES.getlist('imagens')

        for imagem in imagens:
            name = f'{date.today()}-{produto.id}.jpg'

            img = Image.open(imagem)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), f'CONSTRUCT {date.today()}', (255, 255, 255)) 
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(output, 'ImageField', name, 'image/jpeg', sys.getsizeof(output), None)

            imagem = Imagem(imagem=img_final, produto=produto)
            imagem.save()


        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')
        return redirect(reverse('add_produto'))
    
@has_permission_decorator('visualizar_produto')
def produto(request, slug):
    if request.method == 'GET':
        produto = Produto.objects.get(slug=slug)
        form = ProdutoForm(instance=produto)
        
    return render(request, 'produto.html', {'form': form})

