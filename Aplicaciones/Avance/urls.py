from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listadoProyectos/', views.ListadoProyectos, name='listado_proyectos'),
    path('eliminarProyecto/<id>', views.eliminarProyecto, name='eliminarProyecto'),
    path('editarProyecto/<id>', views.editarProyecto, name='editarProyecto'),
    path('guardarProyecto/', views.guardarProyecto, name='guardarProyecto'),
    path('procesoActualizarProyecto/', views.procesoActualizarProyecto, name='procesoActualizarProyecto'),
]
