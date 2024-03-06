from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project, Task, UserWithTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, UserWithTaskSerializer
from .basic_db_command import db_get

def index(request):
    return HttpResponse("")


@api_view(['GET', 'POST', 'DELETE'])
def user_managing(request,id):

    user = User.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(user, UsersSerializer, User)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=200)
        return JsonResponse(user_serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def job_title_managing(request,id):

    job = JobTitle.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(job,JobTitleSerializer,JobTitle)

    # elif request.method == 'POST':
    #     user_data = JSONParser().parse(request)
    #     job_serializer = JobTitleSerializer(data=user_data)
    #     if job_serializer.is_valid():
    #         job_serializer.save()
    #         return JsonResponse(job_serializer.data, status=200)
    #     return JsonResponse(job_serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def project_managing(request,id):
    project = Project.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(project, ProjectSerializer, Project)


def task_managing(request,id):
    task = Task.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(task, TaskSerializer, Task)


def user_with_task_managing(request,id):
    user_with_task = UserWithTask.objects.all().filter(id=id)
    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)
