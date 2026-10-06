from django.shortcuts import render
from django.http import JsonResponse
from .models import Servicio
from rest_framework import viewsets 
from .models import Servicio 
from .serializers import ServicioSerializer 

# Create your views here.

class ServicioViewSet(viewsets.ModelViewSet): 
    queryset = Servicio.objects.all() 
    serializer_class = ServicioSerializer 
  
'''  
def servicio_list(request):
    servicios = list(
    Servicio.objects.filter(activo=True).values("id", "nombre", "descripcion", "precio")
    )
    
    return JsonResponse({"count": len(servicios), "results": servicios})
'''