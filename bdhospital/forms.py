from . import models
from django.forms import ModelForm

class PacienteForm(ModelForm):
    class Meta:
        model = models.Paciente
        fields = ['nombre','numero_seguro','fecha_de_nacimiento']

class MedicoForm(ModelForm):
    class Meta:
        model = models.Medico
        fields = ['nombre','especializacion']

class ConsultaForm(ModelForm):
    class Meta:
        model = models.Consulta
        fields = ['paciente','medico','motivo','diagnostico']

class TratamientoForm(ModelForm):
    class Meta:
        model = models.Tratamiento
        fields = ['medicamento','terapia']

class Paciente_TratemientoForm(ModelForm):
    class Meta:
        model = models.Paciente_Tratamiento
        fields = ['paciente','tratamiento','consulta']