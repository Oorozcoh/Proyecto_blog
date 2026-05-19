from django.db import models
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    autor = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_images', null=True, blank=True)

    def __str__(self):
        return self.titulo