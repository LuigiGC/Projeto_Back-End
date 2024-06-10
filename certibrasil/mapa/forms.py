# forms.py
from django import forms
from .models import Empresa, Endereco, ISO

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_empresa', 'nome', 'email', 'telefone', 'cnpj']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'latitude', 'longitude']

class ISOForm(forms.ModelForm):
    class Meta:
        model = ISO
        fields = ['iso_type', 'odc', 'consultor', 'data_efetivacao', 'validade']
