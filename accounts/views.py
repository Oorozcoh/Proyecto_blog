from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView  # <-- Cambiado a UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm 
from .forms import UserEditForm
from .models import Avatar

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # Recibe los datos enviados
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("Inicio")
    else:
        form = AuthenticationForm()
        
    return render(request, "accounts/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/registro.html", {"form": form})

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'accounts/editar_perfil.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        response = super().form_valid(form)

        if form.cleaned_data.get('imagen'):
            avatar, created = Avatar.objects.get_or_create(user=self.request.user)
            avatar.imagen = form.cleaned_data['imagen']
            avatar.save()

        return response