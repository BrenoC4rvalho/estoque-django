from django.db import models
from produto.models import Produtos

class Saidas(models.Model):
    
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
