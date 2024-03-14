from django import forms
from .models import ArticlesModel

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        fields = [
            'title', 
            'author', 
            'img_destaque',
            'category', 
            'content', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published', 
            #'slug',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['img_destaque'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem Destaque'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord'})
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
            'img_destaque',
            'category', 
            'content', 
            'meta_description', 
            'keyword', 
            'tags',
            'is_published', 
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['img_destaque'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem Destaque'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Texto Rico'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Meta Descrição'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'KeyWord'})

