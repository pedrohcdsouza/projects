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
    first_name = self.cleaned_data.get('first_name', '')
    exists_first_name = User.objects.filter(first_name=first_name).exists()

    if exists_first_name:
        raise ValidationError(
            'A razão social utilizada já está cadastrado no BD.', code='invalid'
        )
    return first_name

def clean_username(self):
    username = self.cleaned_data.get('username', '')
    exists_username = User.objects.filter(username=username).exists()

    if exists_username:
        raise ValidationError(
            'O usuário utilizado já está cadastrado no BD.', code='invalid'
        )
    return username

def clean_email(self):
    email = self.cleaned_data.get('email', '')
    exists = User.objects.filter(email=email).exists()

    if exists:
        raise ValidationError(
            'O e-mail utilizado já está cadastrado no BD.', code='invalid'
        )
    return email