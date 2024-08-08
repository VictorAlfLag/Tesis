from django.urls import path
from . import views
from .views import chart_view



urlpatterns = [

    #GOOGLE CHARTS
    path('chart/', chart_view, name='chart'),
    
    path('', views.home, name='home'),  # Ruta para la página principal
    path('login/', views.login_view, name='login'),  # Ruta para la página de login

    path('listadoProyectos/', views.ListadoProyectos, name='listado_proyectos'),
    path('eliminarProyecto/<id>', views.eliminarProyecto, name='eliminarProyecto'),
    path('editarProyecto/<id>', views.editarProyecto, name='editarProyecto'),
    path('guardarProyecto/', views.guardarProyecto, name='guardarProyecto'),
    path('procesoActualizarProyecto/', views.procesoActualizarProyecto, name='procesoActualizarProyecto'),

    #rutas de convenio
    path('listadoConvenios/', views.ListadoConvenios, name='listado_convenios'),
    path('eliminarConvenio/<id>', views.eliminarConvenio, name='eliminarConvenio'),
    path('editarConvenio/<id>', views.editarConvenio, name='editarConvenio'),
    path('guardarConvenio/', views.guardarConvenio, name='guardarConvenio'),
    path('procesoActualizarConvenio/', views.procesoActualizarConvenio, name='procesoActualizarConvenio'),
    #rutas de articulos
    path('listadoArticulos/', views.ListadoArticulos, name='listado_articulos'),
    path('eliminarArticulo/<id>', views.eliminarArticulo, name='eliminarArticulo'),
    path('editarArticulo/<id>', views.editarArticulo, name='editarArticulo'),
    path('guardarArticulo/', views.guardarArticulo, name='guardarArticulo'),
    path('procesoActualizarArticulo/', views.procesoActualizarArticulo, name='procesoActualizarArticulo'),
    path('nuevoConvenio/', views.nuevoConvenio, name='nuevoConvenio'),
    path('nuevoArticulo/', views.nuevoArticulo, name='nuevoArticulo'),
    path('nuevoProyecto/', views.nuevoProyecto, name='nuevoProyecto'),

]