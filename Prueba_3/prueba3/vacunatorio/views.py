from django.shortcuts import render
from django.http import HttpResponse
from vacunatorio.models import Informacion
from vacunatorio.models import Vacuna
# Create your views here.

def index(request):
    return render(request,"index.html")

def ingresar(request):
    return render(request,"ingresar.html")

def listar(request):
    return render(request,"listar.html")

def buscador(request):
    return render(request,"buscador_vacunados.html")


def ingresar_informacion(request):
    nombre_aux = request.GET["txt_nombre"]
    paterno_aux = request.GET["txt_appaterno"]
    materno_aux = request.GET["txt_apmaterno"]
    rut_aux = request.GET["txt_rut"]
    edad_aux = request.GET["txt_edad"]
    nombre_vacuna_aux = request.GET["txt_vacuna_nombre"]
    fecha = request.GET["fecha"]
    if len(nombre_aux)>0 and len(materno_aux)>0 and len(paterno_aux)>0 and len(rut_aux)>0 and len(edad_aux)>0 and len(nombre_vacuna_aux)>0 and len(fecha)>0:
        pro = Informacion(nombre=nombre_aux, apparteno=paterno_aux, apmaterno=materno_aux ,rut=rut_aux, edad=edad_aux, nombre_vacuna=nombre_vacuna_aux, fecha=fecha)
        pro.save()
        mensaje="Informacion ingresada."
    else:
        mensaje="Debe ingresar la informacion."
    return HttpResponse(mensaje+"<a href='/index/'>Volver al inicio</a>")

def listar_informacion(request):
    datos = Informacion.objects.all()
    return render(request,"listar.html",{'informacion':datos})


def buscar(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        informacion = Informacion.objects.filter(rut__icontains=persona)
        return render(request,"buscador.html",{"informacion":informacion,"query":persona})
    else:
        mensaje = "<h1>Debe ingresar un rut valido...</h1>"
        return HttpResponse(mensaje+"<br><h1><a href='/index/'>Volver al inicio</a></h1>")

# Agregado del examen transversal

def ingreso_vacuna(request):
    return render(request,"ingreso_vacuna.html")

def datos_vacuna(request):
    vacuna_aux=request.GET["txt_nombre_vacuna"]
    fabricante_aux=request.GET["txt_fabricacion"]
    tipo_vacuna_aux=request.GET["txt_tipo_vacuna"]
    lote_aux=request.GET["txt_lote"]
    administracion_aux=request.GET["txt_administracion"]
    if len(vacuna_aux)>0 and len(fabricante_aux)>0 and len(tipo_vacuna_aux)>0 and len(lote_aux)>0 and len(administracion_aux)>0:
        info=Vacuna(vacuna_nombre=vacuna_aux, fabricante=fabricante_aux, tipo_vacuna=tipo_vacuna_aux, lote=lote_aux, forma_administracion=administracion_aux)
        info.save()
        mensaje=("Vacuna ingresada")
    else:
        mensaje=("Error al ingresar la vacuna")
    return HttpResponse(mensaje+"<br><h1><a href='/index/'>Volver al inicio</a></h1>")