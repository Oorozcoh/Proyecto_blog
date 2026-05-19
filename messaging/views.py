from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

# Vista para enviar mensaje (Usa Mixin)
class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = "messaging/enviar_mensaje.html"
    success_url = "/messaging/recibidos/"

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, "messaging/mensajes_list.html", {"mensajes": mensajes})