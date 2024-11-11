from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Paciente, Medico, Consulta, Tratamiento,Paciente_Tratamiento
from .forms import PacienteForm,MedicoForm,ConsultaForm,TratamientoForm,Paciente_TratemientoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    pacientes = Paciente.objects.all()
    medico = Medico.objects.all()
    consulta = Consulta.objects.all()
    tratamiento = Tratamiento.objects.all()
    paciente_tratamiento = Paciente_Tratamiento.objects.all()
    return render(
        request,
        'index.html',
        context={'pacientes':pacientes,'medico':medico,'consulta':consulta,'tratamiento':tratamiento,'paciente_tratamiento':paciente_tratamiento}
    )

@login_required
def paciente(request):
    pacientes = Paciente.objects.all()
    return render(
        request,
        'paciente.html',
        context={'pacientes':pacientes}
    )

@login_required
def medico(request):
    medico = Medico.objects.all()
    return render(
        request,
        'medico.html',
        context={'medico':medico}
    )

@login_required
def consulta(request):
    consulta = Consulta.objects.all()
    return render(
        request,
        'consulta.html',
        context={'consulta':consulta}
    )

@login_required
def tratamiento(request):
    tratamiento = Tratamiento.objects.all()
    return render(
        request,
        'tratamiento.html',
        context={'tratamiento':tratamiento}
    )

@login_required
def paciente_tratamiento(request):
    paciente_tratamiento = Paciente_Tratamiento.objects.all()
    return render(
        request,
        'paciente_tratamiento.html',
        context={'paciente_tratamiento':paciente_tratamiento}
    )

@login_required
def FormPaciente(request): 
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/paciente')
    else:
        form = PacienteForm()
    
    return render(
        request,
        'Paciente/FormPaciente.html',
        {'form': form}
    )

@login_required
def FormMedico(request): 
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')
    else:
        form = MedicoForm()
    
    return render(
        request,
        'Medico/FormMedico.html',
        {'form': form}
    )

@login_required
def FormConsulta(request): 
    paciente = Paciente.objects.all()
    medico = Medico.objects.all()
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/consulta')
    else:
        form = ConsultaForm()
    
    return render(
        request,
        'Consulta/FormConsulta.html',
        {'form': form, 'paciente':paciente, 'medico':medico}
    )

@login_required
def FormTratamiento(request): 
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tratamiento')
    else:
        form = TratamientoForm()
    
    return render(
        request,
        'Tratamiento/FormTratamiento.html',
        {'form': form}
    )

@login_required
def Formpaciente_tratamiento(request): 
    paciente = Paciente.objects.all()
    tratamiento = Tratamiento.objects.all()
    consulta = Consulta.objects.all()
    if request.method == 'POST':
        form = Paciente_TratemientoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/paciente_tratamiento')
    else:
        form = Paciente_TratemientoForm()
    
    return render(
        request,
        'Paciente_Tratamiento/Paciente_Tratamiento.html',
        {'form': form,'paciente':paciente,'tratamiento':tratamiento,'consulta':consulta}
    )

@login_required
def UpdatePaciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/paciente')
    else:
        form  = PacienteForm(instance=paciente)
    return render(
        request,
        'Paciente/UpdatePaciente.html',
        context={'form': form, 'paciente':paciente }
    )

@login_required
def UpdateMedico(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')
    else:
        form  = MedicoForm(instance=medico)
    return render(
        request,
        'Medico/UpdateMedico.html',
        context={'form': form, 'medico':medico }
    )

@login_required
def UpdateConsulta(request, consulta_id):
    paciente = Paciente.objects.all()
    medico = Medico.objects.all()
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/consulta')
    else:
        form  = ConsultaForm(instance=consulta)
    return render(
        request,
        'Consulta/UpdateConsulta.html',
        context={'form': form, 'consulta':consulta,'paciente':paciente,'medico':medico }
    )

@login_required
def UpdateTratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tratamiento')
    else:
        form  = TratamientoForm(instance=tratamiento)
    return render(
        request,
        'Tratamiento/UpdateTratamiento.html',
        context={'form': form }
    )

@login_required
def DeletePaciente(request, paciente_id):
    eliminar = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        eliminar.delete()
        return HttpResponseRedirect('/paciente')
    return render(
        request,
        'Paciente/DeletePaciente.html',
        context={'eliminar': eliminar}
    )

@login_required
def DeleteMedico(request, medico_id):
    eliminar = get_object_or_404(Medico, id=medico_id)
    if request.method == 'POST':
        eliminar.delete()
        return HttpResponseRedirect('/medico')
    return render(
        request,
        'Medico/DeleteMedico.html',
        context={'eliminar': eliminar}
    )

@login_required
def DeleteTratamiento(request, tratamiento_id):
    eliminar = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        eliminar.delete()
        return HttpResponseRedirect('/tratamiento')
    return render(
        request,
        'Tratamiento/DeleteTratamiento.html',
        context={'eliminar': eliminar}
    )

@login_required
def DeleteConsulta(request, consulta_id):
    eliminar = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        eliminar.delete()
        return HttpResponseRedirect('/consulta')
    return render(
        request,
        'Consulta/DeleteConsulta.html',
        context={'eliminar': eliminar}
    )