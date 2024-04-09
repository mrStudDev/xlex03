from django import forms
from .models import ArticlesModel

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        fields = [
            'title', 
            'author', 
            'summary',
            'key_words',
            'category', 
            'content', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published',
            'image',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titulo do Artigo'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sumário'})
        self.fields['key_words'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Palavras Chave do Artigo'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content'].widget.attrs.update({'id': 'editor-content', 'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição SEO'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord SEO'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Images'})
        
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})
            

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        fields = [
            'title', 
            'summary',
            'key_words',
            'category', 
            'content', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published',
            'image',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titulo do Artigo'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sumário'})
        self.fields['key_words'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Palavras Chave do Artigo'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content'].widget.attrs.update({'id': 'editor', 'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição SEO'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord SEO'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Images'})

