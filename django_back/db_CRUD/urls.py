from django.urls import path

from . import views

urlpatterns = [
    path("users/<id>",views.usersManaging),
    path("get_job_title/<id>",views.getJobTitle)
]