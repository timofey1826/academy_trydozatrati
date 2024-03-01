from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project
from .serializer import UsersSerializer, JobTitleSerializer


def index(request):
    return HttpResponse("")
@api_view(['GET', 'POST', 'DELETE'])
def usersManaging(request,id):
    if request.method == 'GET':
        user = User.objects.all().filter(id = id)
        user_serializer = UsersSerializer(user[0])
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=200)
        return JsonResponse(user_serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def getJobTitle(request,id):
    job = JobTitle.objects.all().filter(id = id)
    if request.method == 'GET':
        try:
            job_serializer = JobTitleSerializer(job[0])
            return JsonResponse(job_serializer.data, safe=False)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The job_title does not exist'}, status=404)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        job_serializer = JobTitleSerializer(data=user_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse(job_serializer.data, status=200)
        return JsonResponse(job_serializer.errors, status=400)

@api_view(['GET', 'POST', 'DELETE'])
def ProjectsCRUD(request,pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            project_serializer = JobTitleSerializer(project)
            return JsonResponse(project_serializer.data, safe=True)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=404)
