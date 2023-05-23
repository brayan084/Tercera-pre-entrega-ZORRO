from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'SwissMedical/index.html')

def medicos(request):
    return render(request, 'SwissMedical/crearMedicos.html')

def pacientes(request):
    return render(request, 'SwissMedical/crearPacientes.html')

def citas(request):
    return render(request, 'SwissMedical/crearCitas.html')

def recetas(request):
    return render(request, 'SwissMedical/crearRecetas.html')