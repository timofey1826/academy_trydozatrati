from rest_framework import serializers
from .models import User, JobTitle, Project, Task, UserWithTask


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
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'description'
                  )
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'project_id',
                  'name',
                  'description'
                  )

class UserWithTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWithTask
        fields = ('id',
                  'user_id',
                  'task_id',
                  'status',
                  'work_date',
                  'work_time'
                  )