from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("autor/", crear_autor, name="FormularioAutor"),
    path("categoria/", crear_categoria, name="FormularioSeccion"),
    path("post/", crear_post, name="FormularioPost"),
    path("listar_posts/", PageList.as_view(), name="PagesList"),
    path("buscar/", buscar_post, name="BuscarPost"),
    path("pages/<int:pk>/", PageDetail.as_view(), name="PageDetail"),
    path("About/", about, name="About"),
]
