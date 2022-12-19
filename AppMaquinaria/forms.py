from django import forms

class cosechadoraForm(forms.Form):
    marca=forms.CharField(label="Marca Cosechadora", max_length=50)
    modelo=forms.CharField(label="Modelo Cosechadora", max_length=50)
    plataforma=forms.IntegerField(label="pies de plataforma")
    anio=forms.IntegerField(label="Año de Salida")


class tractorForm(forms.Form):
    marca=forms.CharField(label="Marca Tractor", max_length=50)
    modelo=forms.CharField(label="Modelo Tractor", max_length=50)
    hp=forms.IntegerField(label="Caballos de Fuerza")
    anio=forms.IntegerField(label="Año de Salida")


class aperoForm(forms.Form):
    tipo=forms.CharField(label="Tipo de Apero", max_length=50)
    marca=forms.CharField(label="Marca Apero", max_length=50)
    modelo=forms.CharField(label="Modelo Apero", max_length=50)
    anio=forms.IntegerField(label="Año de Salida")    

