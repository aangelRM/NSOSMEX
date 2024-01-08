# forms.py
from django import forms
from .models import *

from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correoUsuario', 'contraUsuario']  # Solo estos campos

        labels = {
            'correoUsuario': 'Correo Electrónico',
            'contraUsuario': 'Contraseña',
        }

    # Personaliza los mensajes de error
    error_messages = {
        'correoUsuario': {
            'required': 'El campo Correo Electrónico es obligatorio.',
        },
        'contraUsuario': {
            'required': 'El campo Contraseña es obligatorio.',
        },
    }

class SupUsuarioForm(forms.ModelForm):
    class Meta:
        model = SupUsuario
        fields = '__all__'