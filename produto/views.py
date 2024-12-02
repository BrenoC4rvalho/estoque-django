from .models import Cores
from .forms import CorForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

def list_produto(request):
    produtos = Produtos.objects.all()
    template_name = 'list_produto.html'
    context = {
    'produtos': produtos,
    }
    
    return render(request, template_name, context)


def new_cor(request):
    if request.method == 'POST':
        form = CorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cor criada com sucesso!')
            return redirect('produto:list_produto')  # Altere para o destino apropriado
    else:
        form = CorForm()
    
    template_name = 'new_cor.html'
    context = {'form': form}
    return render(request, template_name, context)

def new_produto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:list_produto')
    else:
        template_name = 'new_produto.html'
        context = {
        'form': ProdutoForm(),
        }
        return render(request, template_name, context)
    
def update_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)   
        if form.is_valid():
            form.save()
            return redirect('produto:list_produto')
    
    else:
        template_name = 'update_produto.html'
        context = {
        'form': ProdutoForm(instance=produto),
        'pk': pk,
        }
        return render(request, template_name, context)
    
def delete_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    produto.delete()
    return redirect('produto:list_produto')