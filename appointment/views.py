from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from appointment.models import Appointment
from services.models import Services
from appointment.forms import MakeAppointmentForm
from django.http import HttpResponseForbidden

# Create your views here.
def appointment_status_view(request):
    context = {}

    user = request.user
    try :
        appointments = Appointment.objects.filter(customer_id = user.pk)
        context['appointments'] = appointments
        return render(request, 'appointment/appointment_status.html', context)
    except Appointment.DoesNotExist:
        return render(request, 'appointment/appointment_status.html')

def appointment_list_view(request):
    context = {}

    try :
        appointments = Appointment.objects.all()
        context['appointments'] = appointments
        return render(request, 'appointment/appointment_list.html', context)
    except Appointment.DoesNotExist:
        return render(request, 'appointment/appointment_list.html')


def make_appointment_view(request):
    context = {}

    user = request.user

    if request.POST :
        form = MakeAppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = user
            obj.registration_id = get_new_registration_id()
            print(get_new_registration_id())
            obj.save()
            form = MakeAppointmentForm()
    else :
        form = MakeAppointmentForm()

    services = Services.objects.all()

    context['services'] = services
    context['form'] = form
    context['is_edit'] = False

    return render(request, 'appointment/make_appointment.html', context)

def get_new_registration_id():
    appointment = Appointment.objects.last()

    return appointment.registration_id + 1


def appointment_change_status_view(request, id, status):

    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()

    appointment = get_object_or_404(Appointment, registration_id=id)

    appointment.status = status
    appointment.save()

    if user.is_staff:
        return redirect('appointment:list')
    else:
        return redirect('appointment:status')

def appointment_edit_view(request, id):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return HttpResponseForbidden()

    appointment = get_object_or_404(Appointment, registration_id=id)

    if request.POST :
        form = MakeAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment:list')
    else :
        form = MakeAppointmentForm()

    services = Services.objects.all()

    context['services'] = services
    context['appointment'] = appointment
    context['form'] = form
    context['is_edit'] = True

    return render(request, 'appointment/edit_appointment.html', context)

def appointment_delete_view(request, id):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()

    appointment = get_object_or_404(Appointment, registration_id=id)

    appointment.delete()

    return redirect('appointment:list')