from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm
from produto.models import Produtos

def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {'saidas': saidas}
    return render(request, template_name, context)

def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            saida = form.save(commit=False)
            produto = saida.produto
            
            # Verifica se há estoque suficiente
            if saida.quantidade > produto.quantidade:
                messages.error(request, 'Estoque insuficiente para essa saída.')
            else:
                produto.quantidade -= saida.quantidade
                produto.save()
                saida.save()
                messages.success(request, 'Saída registrada com sucesso!')
                return redirect('saida:list_saida')
    
    else:
        form = SaidaForm()
    
    template_name = 'new_saida.html'
    context = {'form': form}
    return render(request, template_name, context)

def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    quantidade_original = saida.quantidade  # Quantidade antes da edição

    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        if form.is_valid():
            saida = form.save(commit=False)
            produto = saida.produto
            
            # Calcula a quantidade disponível ajustando a saída atual
            quantidade_disponivel = produto.quantidade + quantidade_original
            
            if saida.quantidade > quantidade_disponivel:
                messages.error(request, 'Estoque insuficiente para essa saída.')
            else:
                # Atualiza o estoque com base na diferença
                produto.quantidade = quantidade_disponivel - saida.quantidade
                produto.save()
                saida.save()
                messages.success(request, 'Saída atualizada com sucesso!')
                return redirect('saida:list_saida')
    
    else:
        form = SaidaForm(instance=saida)
    
    template_name = 'update_saida.html'
    context = {'form': form, 'pk': pk}
    return render(request, template_name, context)

def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    produto = saida.produto
    produto.quantidade += saida.quantidade
    produto.save()
    saida.delete()
    return redirect('saida:list_saida')