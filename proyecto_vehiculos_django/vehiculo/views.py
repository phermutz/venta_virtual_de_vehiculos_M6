from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'vehiculo/index.html')

def add_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'add_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.view_catalogo', raise_exception=True)
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    return render(request, 'vehiculo/detalle_vehiculo.html', {'vehiculo': vehiculo})

def add_vehiculo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    
    return render(request, 'vehiculo/lista_vehiculos.html', {'vehiculos': vehiculos})