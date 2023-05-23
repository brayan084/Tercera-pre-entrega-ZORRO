from django.db import models

# Create your models here.

class Medicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Citas(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

class recetas(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=50)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)