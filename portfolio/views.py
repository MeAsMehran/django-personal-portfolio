from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all()   # this line will get all the objects which we created on server and shows it in homepage

    return render(request, "portfolio/homepage.html", {"projects": projects})     # we sent a dictionary which contains all projects