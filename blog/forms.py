
from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()


class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)


class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=30)
