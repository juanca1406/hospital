from django.urls import path
from . import views

app_name = 'Registro'
urlpatterns = [
    path('', views.index, name='index'),
    path('paciente', views.paciente, name='paciente'),
    path('medico', views.medico, name='medico'),
    path('consulta', views.consulta, name='consulta'),
    path('tratamiento', views.tratamiento, name='tratamiento'),
    path('paciente_tratamiento', views.paciente_tratamiento, name='paciente_tratamiento'),
    path('FormMedico', views.FormMedico, name='FormMedico'),
    path('FormPaciente', views.FormPaciente, name='FormPaciente'),
    path('FormConsulta', views.FormConsulta, name='FormConsulta'),
    path('FormTratamiento', views.FormTratamiento, name='FormTratamiento'),
    path('Formpaciente_tratamiento', views.Formpaciente_tratamiento, name='Formpaciente_tratamiento'),
    path('UpdatePaciente/<int:paciente_id>', views.UpdatePaciente, name='UpdatePaciente'),
    path('UpdateMedico/<int:medico_id>', views.UpdateMedico, name='UpdateMedico'),
    path('UpdateConsulta/<int:consulta_id>', views.UpdateConsulta, name='UpdateConsulta'),
    path('UpdateTratamiento/<int:tratamiento_id>', views.UpdateTratamiento, name='UpdateTratamiento'),
    path('DeletePaciente/<int:paciente_id>', views.DeletePaciente, name='DeletePaciente'),
    path('DeleteMedico/<int:medico_id>', views.DeleteMedico, name='DeleteMedico'),
    path('DeleteTratamiento/<int:tratamiento_id>', views.DeleteTratamiento, name='DeleteTratamiento')
]
