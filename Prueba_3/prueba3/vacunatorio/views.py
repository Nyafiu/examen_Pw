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
        mensaje="<h2>Información ingresada</h2>"
    else:
        mensaje="<h2>Debe ingresar la información...</h2>"
    return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")

def listar_informacion(request):
    datos = Informacion.objects.all()
    return render(request,"listar.html",{'informacion':datos})


def buscar(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        informacion = Informacion.objects.filter(rut__icontains=persona)
        return render(request,"buscador.html",{"informacion":informacion,"query":persona})
    else:
        mensaje = "<h2>Debe ingresar un rut válido...</h2>"
        return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")

# Agregado del examen transversal

def ingreso_vacuna(request):
    return render(request,"ingreso_vacuna.html")

def listar_vacunas(request):
    return render(request,"listar_vacuna.html")

def actualizar_vacuna(request):
    return render(request,"actualizar_vacuna.html")

def eliminar_vacuna(request):
    return render(request,"eliminar_vacuna.html")

def buscar_vacuna(request):
    return render(request,"busca_vacuna.html")

def datos_vacuna(request):
    vacuna_aux=request.GET["txt_nombre_vacuna"]
    fabricante_aux=request.GET["txt_fabricacion"]
    tipo_vacuna_aux=request.GET["txt_tipo_vacuna"]
    lote_aux=request.GET["txt_lote"]
    administracion_aux=request.GET["txt_administracion"]
    if len(vacuna_aux)>0 and len(fabricante_aux)>0 and len(tipo_vacuna_aux)>0 and len(lote_aux)>0 and len(administracion_aux)>0:
        info=Vacuna(vacuna_nombre=vacuna_aux, fabricante=fabricante_aux, tipo_vacuna=tipo_vacuna_aux, lote=lote_aux, forma_administracion=administracion_aux)
        info.save()
        mensaje=("<h2>Vacuna ingresada</h2>")
    else:
        mensaje=("<h2>Error al ingresar la vacuna</h2>")
    return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")

def listar_vacuna(request):
    datos = Vacuna.objects.all()
    return render(request,"listar_vacuna.html",{'datos':datos})


def modificar(request):
    if request.GET["txt_id"]:
        id_recibido = request.GET["txt_id"]
        nombre_recibido = request.GET["txt_nombre_vacuna"]
        vacuna = Vacuna.objects.filter(id=id_recibido)
        if vacuna:
            info = Vacuna.objects.get(id=id_recibido)
            info.vacuna_nombre = nombre_recibido
            info.save()
            mensaje = "<h2>La vacuna se actualizó correctamente</h2>"
        else:
            mensaje = "<h2>El id ingresado no existe</h2>"
    else:
        mensaje = "<h2>Debe ingresar un id para modificar...</h2>"
    return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")

def eliminacion_vacuna(request):
    if request.GET["txt_id"]:
        id_recibido = request.GET["txt_id"]
        vacuna = Vacuna.objects.filter(id=id_recibido)
        if vacuna:
            info = Vacuna.objects.get(id=id_recibido)
            info.delete()
            mensaje="<h2>Vacuna eliminada</h2>"
        else:
            mensaje="<h2>No se pudo eliminar la vacuna</h2>"
    else:
        mensaje = "<h2>Debe ingresar un id para eliminar...</h2>"
    return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")

def buscar_vacunas(request):
    if request.GET["txt_id"]:
        id_vacuna = request.GET["txt_id"]
        informacion = Vacuna.objects.filter(id=id_vacuna)
        return render(request,"buscar_vacuna.html",{"informacion":informacion,"query":id_vacuna})
    else:
        mensaje = "<h2>Debe ingresar un id válido...</h2>"
        return HttpResponse(mensaje+"<br><h2><a href='/index/'>Volver al inicio</a></h2>")
