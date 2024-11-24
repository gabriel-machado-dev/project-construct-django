from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Categoria, Produto, Imagem
from datetime import date
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your views here.


def add_produto(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render(request, 'add_produto.html', {'categorias': categorias})
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