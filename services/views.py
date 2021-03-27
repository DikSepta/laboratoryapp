from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from services.models import Services
from services.forms import AddService

# Create your views here.
def service_list_view(request):
    context = {}
    try :
        services = Services.objects.all()
        context['services'] = services
        return render(request, 'services/services.html', context)
    except Services.DoesNotExist:
        return render(request, 'services/services.html')

def service_add_view(request):
    context = {}

    user = request.user

    if request.POST:
        print('success 1')
        form = AddService(request.POST)

        if form.is_valid():
            print('success 2')
            obj = form.save(commit=False)
            service_id = get_new_service_id()
            obj.service_id = service_id
            obj.save()

            return redirect('services:list')

    else :
        form = AddService()

    return render(request, 'services/add_service.html', context)

def get_new_service_id():
    service = Services.objects.last()

    return service.service_id + 1

def service_edit_view(request, id):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return HttpResponseForbidden()

    service = get_object_or_404(Services, service_id=id)

    if request.POST:
        print('success 1')
        form = AddService(request.POST, instance=service)

        if form.is_valid():
            print('success 2')
            form.save()

            return redirect('services:list')

    else :
        form = AddService()
    
    context['service'] = service

    return render(request, 'services/edit_service.html', context)

def service_delete_view(request, id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseForbidden()

    service = get_object_or_404(Services, service_id=id)

    service.delete()

    return redirect('service:list')