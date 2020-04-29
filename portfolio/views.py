from django.shortcuts import render
from .models import Project

def main_about(request):
	return render(request,'portfolio/main_about.html')

def projects(request):
	projects = Project.objects.all()
	return render(request,'portfolio/projects.html',{'projects':projects})#putting the project on the homeepage from database.
