from django import forms
from .models import PrincipiosModel


class CreatePrincipioForm(forms.ModelForm):
    class Meta:
        model = PrincipiosModel
        fields = [
            'principio_name',
            'ramo_direito',
            'content_principio',
            'meta_description',
            'keyword',
            'is_published',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['principio_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome do Principio'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo do Direito'})
        self.fields['content_principio'].widget.attrs.update({'id': 'editor-content-principios', 'class': 'form-control', 'placeholder': 'Texto Do Princípio'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})


class UpdatePrincipioForm(forms.ModelForm):
    class Meta:
        model = PrincipiosModel
        fields = [
            'principio_name',
            'ramo_direito',
            'content_principio',
            'meta_description',
            'keyword',
            'is_published',            
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['principio_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome do Principio'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo do Direito'})
        self.fields['content_principio'].widget.attrs.update({'id': 'editor-content-principios', 'class': 'form-control', 'placeholder': 'Texto Do Princípio'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})
