from django.shortcuts import render, redirect
from .forms import MedicosForm, PacientesForm, CitasForm, recetasForm
from .models import Medicos, Pacientes, Citas, recetas

# Create your views here.
def index(request):
    pacientes_registrados = Pacientes.objects.all()
    medicos_registrados = Medicos.objects.all()
    citas_registradas = Citas.objects.all()
    datos = {
        'medicos': medicos_registrados,
        'pacientes': pacientes_registrados,
        'citas': citas_registradas,
    }
    return render(request, 'SwissMedical/index.html', datos)

# crear medicos
def medicos(request):
    if request.method == 'POST':
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MedicosForm()
    return render(request, 'SwissMedical/crearMedicos.html', {'form': form})

def pacientes(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacientesForm()
    return render(request, 'SwissMedical/crearPacientes.html', {'form': form})

def citas(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CitasForm()
    return render(request, 'SwissMedical/crearCitas.html', {'form': form})

def recetas(request):
    if request.method == 'POST':
        form = recetasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = recetasForm()
    return render(request, 'SwissMedical/crearRecetas.html', {'form': form})