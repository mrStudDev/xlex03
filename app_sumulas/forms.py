from django import forms
from .models import SumulaModel

class CreateSumulaForm(forms.ModelForm):
    class Meta:
        model = SumulaModel
        fields = [
            'title',
            'numero_sumula',
            'sigla_tribunal',
            'nome_tribunal',
            'tema_juridico',
            'turma',
            'enunciado',
            'comentario',
            'meta_description',
            'keyword',
            'is_published', 
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['numero_sumula'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Número da Súmula'})
        self.fields['sigla_tribunal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sigla Tribunal'})
        self.fields['nome_tribunal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Tribunal'})
        self.fields['tema_juridico'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tema Jurídico'})       
        self.fields['turma'].widget.attrs.update({'class': 'form-control', 'placeholder': 'turma'})
        self.fields['enunciado'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enunciado'})
        self.fields['comentario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Comentario'}) 
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})
            

class UpdateSumulaForm(forms.ModelForm):
    class Meta:
        model = SumulaModel
        fields = [
            'title',
            'numero_sumula',
            'sigla_tribunal',
            'nome_tribunal',
            'tema_juridico',
            'turma',
            'enunciado',
            'comentario',
            'meta_description',
            'keyword',
            'is_published', 
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['numero_sumula'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Número da Súmula'})
        self.fields['sigla_tribunal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sigla Tribunal'})
        self.fields['nome_tribunal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Tribunal'})
        self.fields['tema_juridico'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tema Jurídico'})       
        self.fields['turma'].widget.attrs.update({'class': 'form-control', 'placeholder': 'turma'})
        self.fields['enunciado'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enunciado'})
        self.fields['comentario'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Comentario'}) 
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord'})