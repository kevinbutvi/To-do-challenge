from model_utils.models import TimeStampedModel
from django.db import models

# Create your models here.

class Tareas(TimeStampedModel):
    """ Modelo para Tareas """
    
    nombre = models.CharField("Nombre de la Tarea", max_length=50)
    completada = models.BooleanField(default=False)
