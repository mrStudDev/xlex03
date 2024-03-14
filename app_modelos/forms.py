from django import forms
from .models import DocumentsModel

class CreateDocucumentForm(forms.ModelForm):
    class Meta:
        model = DocumentsModel
        fields = [
            'title',
            'document',
            'author',
            'ramo_direito',
            'tipo_doc',
            'content',
            'meta_description',
            'keyword',
            'tags',
            'is_published',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['document'].widget.attrs.update({'class': 'form-control', 'placeholder': 'DOcumento'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo Direito'})
        self.fields['tipo_doc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tipo Doc'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Texto Document'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})



class UpdateDocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentsModel
        fields = [
            'title',
            'document',
            'author',
            'ramo_direito',
            'tipo_doc',
            'content',
            'meta_description',
            'keyword',
            'tags',
            'is_published',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['document'].widget.attrs.update({'class': 'form-control', 'placeholder': 'DOcumento'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo Direito'})
        self.fields['tipo_doc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tipo Doc'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Texto Document'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})

