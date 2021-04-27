from django.shortcuts import render
from projects.models import Project, LandingMessage

def project_index(request):
    projects = Project.objects.all()
    message = LandingMessage.objects.first()
    context = {
        'projects': projects,
        'message': message
    }
    return render(request, 'project_index.html', context)
