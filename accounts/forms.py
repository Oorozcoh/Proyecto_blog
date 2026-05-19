from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")
        
class UserEditForm(forms.ModelForm):
    # Campos que queremos editar del usuario estándar
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'padding: 12px; background: #121824; border: 1px solid #334155; border-radius: 4px; color: #fff;'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'style': 'padding: 12px; background: #121824; border: 1px solid #334155; border-radius: 4px; color: #fff;'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'style': 'padding: 12px; background: #121824; border: 1px solid #334155; border-radius: 4px; color: #fff;'}))
    imagen = forms.ImageField(required=False, label="Cambiar Foto de Perfil")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']