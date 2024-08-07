from django.db import models


# Create your models here.
class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completado', 'Completado'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    docente_encargado = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    documento = models.FileField(upload_to='proyectos', null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
    

class Convenio(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    id = models.AutoField(primary_key=True)
    nombre_convenio = models.CharField(max_length=100)
    entidad = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    documento = models.FileField(upload_to='convenios', null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

    def __str__(self):
        return f"{self.nombre_convenio} - {self.entidad} ({self.estado})"
    
class Articulo(models.Model):
    Q_CHOICES = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    revista = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    impacto_factor = models.FloatField()
    metrica_q = models.CharField(max_length=2, choices=Q_CHOICES)
    documento = models.FileField(upload_to='articulos', null=True, blank=True)
    link_articulo = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.metrica_q})"

    
