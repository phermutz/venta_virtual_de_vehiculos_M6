from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_vehiculo, name='add_vehiculo'),
    path('<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('list/', views.lista_vehiculos, name='lista_vehiculos'),  # Nueva URL para la lista de vehículos
]