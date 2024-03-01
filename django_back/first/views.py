from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User, JobTitle, Project
from .serializer import UsersSerializer, JobTitleSerializer


def index(request):
    return HttpResponse("")
@api_view(['GET', 'POST', 'DELETE'])
def usersManaging(request):
    if request.method == 'GET':
        tutorials = User.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = UsersSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
    tutorial_serializer = UsersSerializer(data=user_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data, status=200)
    return JsonResponse(tutorial_serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def getJobTitle(request,pk):
    tutorial = JobTitle.objects.filter(id = pk)
    print(tutorial)
    if request.method == 'GET':
        try:
            tutorial_serializer = JobTitleSerializer(tutorial[0])
            print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, safe=False)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=404)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        tutorial_serializer = JobTitleSerializer(data=user_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=200)
        return JsonResponse(tutorial_serializer.errors, status=400)

@api_view(['GET', 'POST', 'DELETE'])
def ProjectsCRUD(request,pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            project_serializer = JobTitleSerializer(project)
            return JsonResponse(project_serializer.data, safe=True)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=404)
