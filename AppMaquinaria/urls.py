from django.urls import path
from .views import *


urlpatterns = [
    
    path("cosechadora/", cosechadora, name="cosechadora"),
    path("tractor/", tractor, name="tractor"),
    path("apero/", apero, name="apero"),
    path("", inicio, name="inicio"),

    path("cosechadoraFormulario/", cosechadoraFormulario, name="cosechadoraFormulario" ),
    path("tractorFormulario/", tractorFormulario, name="tractorFormulario"),
    path("aperoFormulario/", aperoFormulario, name="aperoFormulario"),

    path("busquedaCosechadora/", busquedaCosechadora, name="busquedaCosechadora"),
    path("buscar/", buscar, name="buscar")
    



]