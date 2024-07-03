from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta: 
        model = Contacto 
        fields = ['nombre','email','mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'forms-control'}),
            'email': forms.EmailInput(attrs={'class': 'forms-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'forms-control'}),

        }