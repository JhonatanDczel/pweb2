from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def hello(request, username):
  print(username)
  return HttpResponse(f"Hello, {username}!")


def index(request):
  return HttpResponse("<h1>Index Page<h1>")


def projects(request):
  projects = Project.objects.values()
  projects = list(projects)
  return JsonResponse(projects, safe=False)


def tasks(request, id):
  task = get_object_or_404(Task, id=id)
  return HttpResponse(f"task: {task.title}")
