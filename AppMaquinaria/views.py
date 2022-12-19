from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from AppMaquinaria.forms import cosechadoraForm, tractorForm, aperoForm

# Create your views here.

def cosechadora (request):
    return render (request, "AppMaquinaria/cosechadora.html")


def tractor (request):
    return render (request, "AppMaquinaria/tractor.html")


def apero (request):
    return render (request, "AppMaquinaria/apero.html")


def inicio (request):
    return render (request, "AppMaquinaria/inicio.html")


def cosechadoraFormulario(request):
    if request.method=="POST":
        form=cosechadoraForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            marca=informacion["marca"]
            modelo=informacion["modelo"]
            plataforma=informacion["plataforma"]
            anio=informacion["anio"]
            cosechadora=Cosechadora(marca=marca, modelo=modelo, plataforma=plataforma, anio=anio)
            cosechadora.save()
            return render (request, "AppMaquinaria/inicio.html", {"mensaje": "Cosechadora Guardada Corectamente"})
        else:
            return render (request, "AppMaquinaria/cosechadoraFormulario.html", {"form": form, "mensaje": "Info no Valida"})
        
    else:
        formulario=cosechadoraForm()
        return render (request, "AppMaquinaria/cosechadoraFormulario.html", {"form": formulario})


def tractorFormulario(request):
    if request.method=="POST":
        form=tractorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            marca=informacion["marca"]
            modelo=informacion["modelo"]
            hp=informacion["hp"]
            anio=informacion["anio"]
            tractor=Tractor(marca=marca, modelo=modelo, hp=hp, anio=anio)
            tractor.save()
            return render (request, "AppMaquinaria/inicio.html", {"mensaje": "Tractor Guardado Corectamente"})
        else:
            return render (request, "AppMaquinaria/tractorFormulario.html", {"form": form, "mensaje": "Info no Valida"})
        
    else:
        formulario=tractorForm()
        return render (request, "AppMaquinaria/tractorFormulario.html", {"form": formulario})


def aperoFormulario(request):
    if request.method=="POST":
        form=aperoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            tipo=informacion["tipo"]
            marca=informacion["marca"]
            modelo=informacion["modelo"]
            anio=informacion["anio"]
            apero=Apero(tipo=tipo, marca=marca, modelo=modelo, anio=anio)
            apero.save()
            return render (request, "AppMaquinaria/inicio.html", {"mensaje": "Apero Guardado Corectamente"})
        else:
            return render (request, "AppMaquinaria/aperoFormulario.html", {"form": form, "mensaje": "Info no Valida"})
        
    else:
        formulario=aperoForm()
        return render (request, "AppMaquinaria/aperoFormulario.html", {"form": formulario})


def busquedaCosechadora (request):
    return render (request, "AppMaquinaria/busquedaCosechadora.html")


def buscar (request):
    marca=request.GET["marca"]
    if marca!="":
        cosechadoras= Cosechadora.objects.filter (marca__icontains=marca)
        return render (request, "AppMaquinaria/resultadosBusqueda.html", {"cosechadoras":cosechadoras})
    else:
        return render (request, "AppCoder/busquedaCosechadora.html", {"mensaje":"por favor ingrese una Cosechadora!"})
