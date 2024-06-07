from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.
def hello(request, username):
  print(username)
  return HttpResponse(f"Hello, {username}!")


def index(request):
  title = "Welcome to Django Project!"
  return render(request, 'index.html', {'title': title})


def about(request):
  return render(request, 'about.html')


def projects(request):
  projects = Project.objects.values()
  return render(request, 'projects.html', {'projects': projects})


def tasks(request):
  tasks = Task.objects.all()
  return render(request, 'tasks.html', {'tasks': tasks})
