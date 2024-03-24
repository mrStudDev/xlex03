from django import forms
from .models import ArticlesSocialModel

class CreateArticleSocialForm(forms.ModelForm):
    class Meta:
        model = ArticlesSocialModel
        fields = [
            'title', 
            'author', 
            'summary',
            'key_words',
            'category', 
            'content_social', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published', 
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titulo do Artigo'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sumário'})
        self.fields['key_words'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Palavras Chave do Artigo'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content_social'].widget.attrs.update({'id': 'editor-content-social', 'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição SEO'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord SEO'})
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})
            

class UpdateArticleSocialForm(forms.ModelForm):
    class Meta:
        model = ArticlesSocialModel
        fields = [
            'title', 
            'summary',
            'key_words',
            'category', 
            'content_social', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published', 
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titulo do Artigo'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sumário'})
        self.fields['key_words'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Palavras Chave do Artigo'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content_social'].widget.attrs.update({'id': 'editor-content-social', 'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição SEO'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord SEO'})

