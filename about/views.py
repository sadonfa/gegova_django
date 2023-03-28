from django.shortcuts import render
from about.models import About, Team

# Create your views here.
def about(request):

    about = About.objects.all()
    teams = Team.objects.all()

    return render(request, 'about.html', {
        'titulo': 'Nosotros',
        'cont_about': about,
        'teams': teams
    })