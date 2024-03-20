from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project, Task, UserWithTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, UserWithTaskSerializer
from .basic_db_command import db_get, db_create


def index(request):
    return HttpResponse("")


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_managing(request, id):
    user = User.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(user, UsersSerializer, User)

    elif request.method == 'POST':
        return db_create(request, UsersSerializer)

    elif request.method == 'PUT':
        return db_create(request, UsersSerializer, id)


@api_view(['GET', 'POST', 'DELETE'])
def job_title_managing(request, id):
    job = JobTitle.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(job, JobTitleSerializer, JobTitle)

    elif request.method == 'POST':
        return db_create(request, JobTitleSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def project_managing(request, id):
    project = Project.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(project, ProjectSerializer, Project)

    elif request.method == 'POST':
        return db_create(request, ProjectSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def task_managing(request, id):
    task = Task.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(task, TaskSerializer, Task)

    elif request.method == 'POST':
        return db_create(request, TaskSerializer)


@api_view(['GET', 'POST', 'DELETE'])
def user_with_task_managing(request, id):
    user_with_task = UserWithTask.objects.all().filter(id=id)

    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)

    elif request.method == 'POST':
        return db_create(request, UserWithTaskSerializer)
