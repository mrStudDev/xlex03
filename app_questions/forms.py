
from django import forms
from django.forms import widgets
from .models import XlexQuestionModel, AlternativasModel

class CreateXlexQuestionForm(forms.ModelForm):
    class Meta:
        model = XlexQuestionModel
        fields = ['title', 'banca', 'disciplina', 'ramo_direito', 'question_ask', 'fundaments', 'tags', 'meta_description', 'keyword','is_published',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['banca'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Banca'})
        self.fields['disciplina'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Disciplina'})
        self.fields['ramo_direito'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ramo Direito'})
        self.fields['question_ask'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Questão'})
        self.fields['fundaments'].widget.attrs.update({'id': 'editor-fundaments', 'class': 'form-control', 'placeholder': 'Fundamentação'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tag'})
        self.fields['meta_description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição'})
        self.fields['keyword'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Key Word'})
        #self.fields['code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'code'})
        
        # Lógica condicional para o campo is_published
        if isinstance(self.fields['is_published'].widget, forms.CheckboxInput):
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
        else:
            self.fields['is_published'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Is Published'})


class CreateXlexAnswerForm(forms.ModelForm):
    class Meta:
        model = AlternativasModel
        fields = ['question', 'text', 'is_correct']
        widgets = {
            'question': forms.Select(),
            'text': forms.Textarea(attrs={'rows': 4}),
        }