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
            produto.quantidade -= saida.quantidade
            produto.save()
            saida.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'new_saida.html'
        context = {'form': SaidaForm()}
        return render(request, template_name, context)

def update_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        if form.is_valid():
            saida = form.save(commit=False)
            produto = saida.produto
            produto.quantidade -= saida.quantidade
            produto.save()
            saida.save()
            return redirect('saida:list_saida')
    else:
        template_name = 'update_saida.html'
        context = {'form': SaidaForm(instance=saida), 'pk': pk}
        return render(request, template_name, context)

def delete_saida(request, pk):
    saida = Saidas.objects.get(pk=pk)
    produto = saida.produto
    produto.quantidade += saida.quantidade
    produto.save()
    saida.delete()
    return redirect('saida:list_saida')