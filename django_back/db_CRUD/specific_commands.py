from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project, Task, UserWithTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, UserWithTaskSerializer
from .basic_db_command import db_get


@api_view(['GET', 'POST', 'DELETE'])
def get_all_job_titles(request):

    job_title = JobTitle.objects.all()
    if request.method == 'GET':
        return db_get(job_title, JobTitleSerializer, JobTitle)


def get_all_user_task(request, user_id):
    user_with_task = UserWithTask.objects.all().filter(user_id=user_id)
    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)

