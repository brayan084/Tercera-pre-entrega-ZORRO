from django.shortcuts import render
from .forms import MedicosForm, PacientesForm, CitasForm, recetasForm

# Create your views here.
def index(request):
    return render(request, 'SwissMedical/index.html')

# crear medicos
def medicos(request):
    if request.method == 'POST':
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MedicosForm()
    return render(request, 'SwissMedical/crearMedicos.html', {'form': form})

def pacientes(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PacientesForm()
    return render(request, 'SwissMedical/crearPacientes.html', {'form': form})

def citas(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CitasForm()
    return render(request, 'SwissMedical/crearCitas.html', {'form': form})

def recetas(request):
    if request.method == 'POST':
        form = recetasForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = recetasForm()
    return render(request, 'SwissMedical/crearRecetas.html', {'form': form})