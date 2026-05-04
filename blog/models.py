
from django.db import models

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
