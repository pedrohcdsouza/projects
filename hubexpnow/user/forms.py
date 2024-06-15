from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Razão social'
        }

        help_texts = {
            
        }

        errors_messages = {

        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite a razão social da empresa.'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite o usuário da empresa.'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite o e-mail válido da empresa.'
            }),
            
        }
def clean_first_name(self):
    data = self.cleaned_data.get('first_name')
    
    return data