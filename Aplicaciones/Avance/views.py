from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Proyecto
from django.contrib import messages
from .models import Convenio
from .models import Articulo
from datetime import date, datetime

def home(request):
    return render(request, 'home.html')
def login_view(request):
    return render(request, 'login.html')

def chart_view(request):
    articulos = Articulo.objects.all()  # Recupera todos los artículos de la base de datos

    # Recopila datos para el gráfico (por ejemplo, título y impacto)
    data_for_chart = [[articulo.titulo, articulo.impacto_factor] for articulo in articulos]

    return render(request, 'chart.html', {
        'articulos': articulos,
        'data_for_chart': data_for_chart
    })




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
    today = date.today()  # Obtiene la fecha actual

    for convenio in convenios:
        convenio.dias_restantes = (convenio.fecha_fin - today).days  # Calcula los días restantes

    return render(request, "listadoConvenios.html", {'convenios': convenios, 'today': today})

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



def ListadoArticulos(request):
    articulos = Articulo.objects.all()

    # Preparar los datos para el gráfico
    chart_data = []
    for articulo in articulos:
        chart_data.append((articulo.titulo, articulo.impacto_factor))

    return render(request, "listadoArticulos.html", {
        'articulos': articulos,
        'chart_data': chart_data
    })
    
    return render(request, "listadoArticulos.html", context)


def nuevoArticulo(request):
    return render(request, 'nuevoArticulo.html')

def guardarArticulo(request):
    titulo = request.POST['titulo']
    autor = request.POST['autor']
    revista = request.POST['revista']
    fecha_publicacion = request.POST['fecha_publicacion']
    impacto_factor = request.POST['impacto_factor']
    metrica_q = request.POST['metrica_q']
    documento = request.FILES.get('documento')
    link_articulo = request.POST['link_articulo']
    Articulo.objects.create(
        titulo=titulo,
        autor=autor,
        revista=revista,
        fecha_publicacion=fecha_publicacion,
        impacto_factor=impacto_factor,
        metrica_q=metrica_q,
        documento=documento,
        link_articulo=link_articulo
    )
    messages.success(request, "Artículo registrado exitosamente.")
    return redirect('listado_articulos')

def editarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    return render(request, 'editarArticulo.html', {'articulo': articulo})

def procesoActualizarArticulo(request):
    id = request.POST['id']
    titulo = request.POST['titulo']
    autor = request.POST['autor']
    revista = request.POST['revista']
    fecha_publicacion = request.POST['fecha_publicacion']
    impacto_factor = request.POST['impacto_factor']
    metrica_q = request.POST['metrica_q']
    articulo = Articulo.objects.get(id=id)
    articulo.titulo = titulo
    articulo.autor = autor
    articulo.revista = revista
    articulo.fecha_publicacion = fecha_publicacion
    articulo.impacto_factor = impacto_factor
    articulo.metrica_q = metrica_q
    if request.FILES.get('documento'):
        articulo.documento = request.FILES.get('documento')
    articulo.link_articulo = request.POST['link_articulo']
    articulo.save()
    messages.success(request, "Artículo actualizado correctamente")
    return redirect('listado_articulos')

def eliminarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    articulo.delete()
    messages.success(request, "Artículo eliminado exitosamente.")
    return redirect('listado_articulos')

def chart_view(request):
    # Lógica de la vista
    return render(request, 'template_name.html', context)