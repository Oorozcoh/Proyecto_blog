from django.shortcuts import render
from .models import Autor, Categoria, Post, Page
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, "blog/inicio.html")

def crear_autor(request):
    if request.method == "POST":
        formulario = AutorFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Autor.objects.create(**datos)
            return render(request, "blog/inicio.html")
    else:
        formulario = AutorFormulario()
    return render(request, "blog/crear_autor.html", {"formulario": formulario})

def crear_categoria(request):
    formulario = CategoriaFormulario(request.POST or None)
    if formulario.is_valid():
        Categoria.objects.create(**formulario.cleaned_data)
        return render(request, "blog/inicio.html")
    return render(request, "blog/crear_categoria.html", {"formulario": formulario})

def crear_post(request):
    formulario = PostFormulario(request.POST or None)
    if formulario.is_valid():
        Post.objects.create(**formulario.cleaned_data)
        return render(request, "blog/inicio.html")
    return render(request, "blog/crear_post.html", {"formulario": formulario})

from django.shortcuts import render
from .models import Post

from django.shortcuts import render
from .models import Post

def buscar_post(request):
    posts = None  # 👈 importante
    hay_busqueda = False

    titulo = request.GET.get("titulo")
    autor = request.GET.get("autor")
    categoria = request.GET.get("categoria")

    if titulo or autor or categoria:
        hay_busqueda = True
        posts = Post.objects.all()

        if titulo:
            posts = posts.filter(titulo__icontains=titulo)

        if autor:
            posts = posts.filter(autor__icontains=autor)

        if categoria:
            posts = posts.filter(categoria__icontains=categoria)

    return render(
        request,
        "blog/buscar.html",
        {
            "posts": posts,
            "hay_busqueda": hay_busqueda
        }
    )

def listar_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/listar_posts.html", {"posts": posts})

class PageList(ListView):
    model = Post
    template_name = "blog/listar_posts.html"
    context_object_name = "posts"


class PageDetail(DetailView):
    model = Page
    template_name = "blog/detalle_post.html"

class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = "/pages/"
    
def about(request):
    return render(request, "blog/about.html")