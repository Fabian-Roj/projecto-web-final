from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter 
from .views import ServicioViewSet 

router = DefaultRouter() 
router.register("servicios", ServicioViewSet, basename="servicio") 

urlpatterns = router.urls

'''
urlpatterns = [
    path("servicios/", views.servicio_list, name="servicio-list"),
]
'''