from django.contrib import admin
from .models import Paciente, Medico, Consulta, Tratamiento, Paciente_Tratamiento
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','numero_seguro','fecha_de_nacimiento')

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','especializacion')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','paciente','medico','fecha','motivo','diagnostico')

class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id','medicamento','terapia')

class Paciente_TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id','paciente','tratamiento','consulta')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Paciente_Tratamiento, Paciente_TratamientoAdmin)
