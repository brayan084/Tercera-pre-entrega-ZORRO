from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicos/', views.medicos, name='crearMedicos'),
    path('pacientes/', views.pacientes, name='crearPacientes'),
    path('citas/', views.citas, name='crearCitas'),
    path('recetas/', views.recetas, name='crearRecetas'),
    path('verRecetas/', views.verRecetas , name='verRecetas'),
]