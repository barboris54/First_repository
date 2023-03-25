from django.shortcuts import render
from .models import My_skills

def index(request):
    projects = My_skills.objects.all()
    return render(request, 'my_skills/index.html', {'projects': projects})
