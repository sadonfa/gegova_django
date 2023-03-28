from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):

    services = Service.objects.all()

    return render(request, 'servicios.html', {
        'titulo': 'Nuestros Servicios',
        'services': services
    })