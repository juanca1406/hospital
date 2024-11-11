from django.db import models
from django.utils import timezone

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    numero_seguro = models.IntegerField(unique=True)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    especializacion = models.CharField(max_length=255)

    def __str__(self):
        return self.especializacion

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    motivo  = models.CharField(max_length=255)
    diagnostico = models.CharField(max_length=255)

    def __str__(self):
       return self.fecha.strftime("%d-%m-%Y")
    
class Tratamiento(models.Model):
    medicamento = models.CharField(max_length=255)
    terapia =  models.CharField(max_length=255)

    def __str__(self):
        return self.medicamento

class Paciente_Tratamiento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)