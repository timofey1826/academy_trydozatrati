from rest_framework import serializers
from .models import User, JobTitle


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'job_title_id',
                  'age',
                  'first_name',
                  'last_name',
                  'father_name',
                  'login',
                  'password')
class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ('id',
                  'name'
                  )
