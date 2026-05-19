from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import login_request, register, EditarPerfilView

urlpatterns = [
    # Login y Logout
    path('login/', login_request, name='Login'),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='Logout'),
   
    # Perfil
    path('perfil/', EditarPerfilView.as_view(), name='EditarPerfil'),
    path('password/', PasswordChangeView.as_view(template_name='accounts/cambiar_password.html', success_url='/accounts/password/exito/'), name='CambiarPassword'),
    path('password/exito/', PasswordChangeDoneView.as_view(template_name='accounts/password_exito.html'), name='PasswordChangeDone'),
]