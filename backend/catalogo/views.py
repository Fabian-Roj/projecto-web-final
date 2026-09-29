from django.shortcuts import render
from django.http import JsonResponse
from .models import Servicio

# Create your views here.

def servicio_list(request):
    servicios = list(
    Servicio.objects.filter(activo=True).values("id", "nombre", "descripcion", "precio")
    )
    
    return JsonResponse({"count": len(servicios), "results": servicios})