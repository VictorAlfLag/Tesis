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