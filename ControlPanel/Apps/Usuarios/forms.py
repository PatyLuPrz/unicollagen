from django import forms
from Apps.Usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'nombre_usuario',
            'apellido_paterno_usuario',
            'apellido_materno_usuario',
            'correo_usuario',
            'contrasena_usuario',
        ]
        labels = {
            'nombre_usuario':'Nombre de usuario',
            'apellido_paterno_usuario':'Apellido paterno',
            'apellido_materno_usuario':'Apellido materno',
            'correo_usuario':'Correo electronico',
            'contrasena_usuario':'Contraseña',
        }
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'correo_usuario': forms.EmailInput(attrs={'class':'form-control'}),
            'contrasena_usuario': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class UsuarioNoPasswordForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'nombre_usuario',
            'apellido_paterno_usuario',
            'apellido_materno_usuario',
            'correo_usuario',
        ]
        labels = {
            'nombre_usuario':'Nombre de usuario',
            'apellido_paterno_usuario':'Apellido paterno',
            'apellido_materno_usuario':'Apellido materno',
            'correo_usuario':'Correo electronico',
        }
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'correo_usuario': forms.EmailInput(attrs={'class':'form-control'}),
        }
