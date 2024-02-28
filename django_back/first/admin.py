from django.contrib import admin

from .models import JobTitle, Project, Task, User, WorkOnTask

admin.site.register(JobTitle)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(WorkOnTask)
