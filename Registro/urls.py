from django.urls import path
from Registro.views import registrar, ver_logs, home, ver_fondos

urlpatterns = [
    # LINK[epic=url] Url en app
    path('', home, name="Home"),
    path('registrar', registrar, name="Registrar"),
    path('registrar/<str:tipo>', registrar, name="RegistrarTrade"),
    path('ver_logs', ver_logs, name="Ver Registros"),
    path('ver_fondos', ver_fondos, name="Ver Fondos"),
]