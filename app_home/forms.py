# Forms Messages

from django import forms

from .models import ContactMessagesModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessagesModel
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Assunto'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Menssagem'})
        
