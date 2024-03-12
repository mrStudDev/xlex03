
from django import forms
from app_sumulas.models import SumulaModel
from app_juris_stj.models import STJjurisprudenciaModel

# Universal Forms Search Juris STJ
class UniversalSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255, 
        required=True, 
        label="Pesquisa",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua pesquisa...'})
    )

# Adavanced Forms Search Juris STJ
class AdvancedSearchForm(forms.ModelForm):
    # Filtrar por ementa com um campo de texto
    ementa = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ementa...'}))

    # Filtrar por período com dois campos de data
    data_formatada_inicial = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    data_formatada_final = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    # ... outros campos ...

    # Filtrar por numeroProcesso, descricaoClasse e ministroRelator com campos de texto
    numeroProcesso = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Número do Processo...'}))
    descricaoClasse = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Descrição da Classe...'}))
    ministroRelator = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ministro Relator...'}))

    class Meta:
        model = STJjurisprudenciaModel
        fields = [
            'ementa', 
            'data_formatada_inicial', 
            'data_formatada_final',
            'descricaoClasse', 
            'numeroProcesso',  
            'ministroRelator'
            ]



class SumulaSearchForm(forms.ModelForm):
    # Filtrar por ementa com um campo de texto
    enunciado = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ementa...'}))
    sigla_tribunal = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Sigla Tribunal...'}))
    numero_sumula = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Número da Súmula...'}))
    nome_tribunal = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nome do Tribunal'}))
    tema_juridico = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Tema Jurídico...'}))

    class Meta:
        model = SumulaModel
        fields = [
            'enunciado', 
            'sigla_tribunal',
            'numero_sumula', 
            'nome_tribunal',
            'tema_juridico'
            ]
