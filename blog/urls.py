from django.urls import path
from .views import *

urlpatterns = [
    path("", lambda r: render(r, "blog/inicio.html")),
    path("autor/", crear_autor),
    path("categoria/", crear_categoria),
    path("post/", crear_post),
    path("listar_posts/", listar_posts, name="listar_posts"),
    path("buscar/", buscar_post),
    
]
