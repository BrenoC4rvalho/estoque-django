from django.forms import ModelForm
from .models import Produtos
from .models import Cores

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']

class CorForm(ModelForm):
    class Meta:
        model = Cores
        fields = ['cor']