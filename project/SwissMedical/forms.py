from django import forms
from .models import Medicos, Pacientes, Citas, recetas

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['nombre', 'apellido', 'especialidad']
    
class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido']

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['medico', 'paciente', 'fecha']

class recetasForm(forms.ModelForm):
    class Meta:
        model = recetas
        fields = ['descripcion', 'fecha', 'medico', 'paciente']
    
