from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def medicos(request):
    return render(request, 'crearMedicos.html')