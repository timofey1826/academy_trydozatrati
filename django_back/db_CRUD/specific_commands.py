from datetime import datetime

import jwt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import AuthenticationFailed

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


class RegisterView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        login = data['login']
        password = data['password']
        user = User.objects.filter(login=login).first()
        if user is None:
            raise AuthenticationFailed('Нету такого пользователя')
        if not user.password == password:
            raise AuthenticationFailed('Неверный пароль')
        payload = {
            'user': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'Успешно логинизировлись',
            'token': token
        }
        return response


class UserView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if token is None:
            raise AuthenticationFailed({'message': 'Ты не аутетифицирован '}, status=401)
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Токен истек', status=401)
        user = User.objects.filter(id=payload['user']).first()
        serialize = UsersSerializer(user)
        return Response({'message': 'Ты аутетифицирован', 'token': token, 'userData': serialize.data})