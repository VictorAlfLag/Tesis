from django.shortcuts import render, redirect
from .models import Proyecto
from django.contrib import messages
from .models import Convenio
from datetime import datetime

def home(request):
    return render(request,"home.html")  


def ListadoProyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "listadoProyectos.html", {'proyectos': proyectos})

def nuevoProyecto(request):
    return render(request, 'nuevoProyecto.html')

def guardarProyecto(request):
    nombre = request.POST['nombre']
    docente_encargado = request.POST['docente_encargado']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    documento = request.FILES.get('documento')
    estado = request.POST['estado']
    Proyecto.objects.create(
        nombre=nombre,
        docente_encargado=docente_encargado,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        documento=documento,
        estado=estado
    )
    messages.success(request, "Proyecto registrado exitosamente.")
    return redirect('listado_proyectos')

def editarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, 'editarProyecto.html', {'proyecto': proyecto})

def procesoActualizarProyecto(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    docente_encargado = request.POST['docente_encargado']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    estado = request.POST['estado']
    proyecto = Proyecto.objects.get(id=id)
    proyecto.nombre = nombre
    proyecto.docente_encargado = docente_encargado
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin
    proyecto.estado = estado
    if request.FILES.get('documento'):
        proyecto.documento = request.FILES.get('documento')
    proyecto.save()
    messages.success(request, "Proyecto actualizado correctamente")
    return redirect('listado_proyectos')

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    messages.success(request, "Proyecto eliminado exitosamente.")
    return redirect('listado_proyectos')


def ListadoConvenios(request):
    convenios = Convenio.objects.all()
    return render(request, "listadoConvenios.html", {'convenios': convenios})

def nuevoConvenio(request):
    return render(request, 'nuevoConvenio.html')

def guardarConvenio(request):
    nombre_convenio = request.POST['nombre_convenio']
    entidad = request.POST['entidad']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    documento = request.FILES.get('documento')
    estado = request.POST['estado']
    Convenio.objects.create(
        nombre_convenio=nombre_convenio,
        entidad=entidad,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        documento=documento,
        estado=estado
    )
    messages.success(request, "Convenio registrado exitosamente.")
    return redirect('listado_convenios')

def editarConvenio(request, id):
    convenio = Convenio.objects.get(id=id)
    return render(request, 'editarConvenio.html', {'convenio': convenio})

def procesoActualizarConvenio(request):
    id = request.POST['id']
    nombre_convenio = request.POST['nombre_convenio']
    entidad = request.POST['entidad']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    estado = request.POST['estado']
    convenio = Convenio.objects.get(id=id)
    convenio.nombre_convenio = nombre_convenio
    convenio.entidad = entidad
    convenio.fecha_inicio = fecha_inicio
    convenio.fecha_fin = fecha_fin
    convenio.estado = estado
    if request.FILES.get('documento'):
        convenio.documento = request.FILES.get('documento')
    convenio.save()
    messages.success(request, "Convenio actualizado correctamente")
    return redirect('listado_convenios')

def eliminarConvenio(request, id):
    convenio = Convenio.objects.get(id=id)
    convenio.delete()
    messages.success(request, "Convenio eliminado exitosamente.")
    return redirect('listado_convenios')
