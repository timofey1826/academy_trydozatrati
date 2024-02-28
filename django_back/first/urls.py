from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users",views.usersManaging),
    path("get_job_title/1",views.getJobTitle)
]