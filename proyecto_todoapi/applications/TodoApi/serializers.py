from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Tareas


class TareaSerializer(serializers.ModelSerializer):
    """ Serializador para Tareas """
    
    class Meta:
        model = Tareas
        fields = ("__all__")
