from django.shortcuts import render
from .forms import MedicosForm

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
    return render(request, 'SwissMedical/crearPacientes.html')

def citas(request):
    return render(request, 'SwissMedical/crearCitas.html')

def recetas(request):
    return render(request, 'SwissMedical/crearRecetas.html')