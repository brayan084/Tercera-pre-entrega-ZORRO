from django import forms
from .models import Medicos, Pacientes, Citas, recetas

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['nombre', 'apellido', 'especialidad']
    
