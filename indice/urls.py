from .views import inicio, mi_plantilla, numero_del_usuario, otra_vista, numero_random, numero_del_usuario, mi_plantilla
from django.urls import path

urlpatterns = [
    path("", inicio),
    path("", otra_vista),
    path("numero-random/", numero_random),
    path("dame-numero/<int:numero>", numero_del_usuario),
    path("mi-plantilla", mi_plantilla),
]
    