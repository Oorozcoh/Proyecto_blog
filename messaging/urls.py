from django.urls import path
from .views import EnviarMensaje, lista_mensajes

urlpatterns = [
    path('enviar/', EnviarMensaje.as_view(), name="EnviarMensaje"),
    path('recibidos/', lista_mensajes, name="MensajesList"),
]