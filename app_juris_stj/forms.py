from django import forms
from .models import STJJurisprudenciaUpload


class STJJurisprudenciaUploadForm(forms.ModelForm):
    class Meta:
        model = STJJurisprudenciaUpload
        fields = ['title', 'upload', 'description',]


class JurisprudenciaSearchEmentaForm(forms.Form):
    termo_ementa = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Encontre uma jurisprudência'}))
