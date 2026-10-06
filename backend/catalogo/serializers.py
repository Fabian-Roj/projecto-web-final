from rest_framework import serializers
from .models import Servicio

class ServicioSerializer  (serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ["id", "nombre", "descripcion", "precio", "activo", "creado_en"] 
        read_only_fields = ["id", "creado_en"]
        
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que 0")
        return value