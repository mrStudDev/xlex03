from django import forms
from .models import CasoConcretoModel


class CreateCasoForm(forms.ModelForm):
    class Meta:
        model = CasoConcretoModel
        fields = [
            'title',
            'disciplina',
            'ramo_direito',
            'pergunta_caso',
            'resposta_caso',
            'fundamentacao',
            'meta_description',
            'keyword',
            'tags',
            'is_published',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['disciplina'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Disciplina'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo do Direito'})
        self.fields['pergunta_caso'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pergunta caso'})
        self.fields['resposta_caso'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Resposta caso'})
        self.fields['fundamentacao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Fundamentação'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})


class UpdateCasoForm(forms.ModelForm):
    class Meta:
        model = CasoConcretoModel
        fields = [
            'title',
            'disciplina',
            'ramo_direito',
            'pergunta_caso',
            'resposta_caso',
            'fundamentacao',
            'meta_description',
            'keyword',
            'tags',
            'is_published',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['disciplina'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Disciplina'})
        self.fields['pergunta_caso'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pergunta caso'})
        self.fields['resposta_caso'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Resposta caso'})
        self.fields['fundamentacao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Fundamentação'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})
