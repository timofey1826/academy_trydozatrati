from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import User
from .serializer import UsersSerializer

def db_get(objects = [],Serializer = UsersSerializer(),curent_class = User()):
    send_data = []

    try:
        for i in objects:
            serializer = Serializer(i)
            send_data.append(serializer.data)
        if len(send_data) == 1:
            return JsonResponse(send_data[0], safe=False)
        return JsonResponse(send_data, safe=False)

    except curent_class.DoesNotExist:
        return JsonResponse({'message': 'The job_title does not exist'}, status=404)