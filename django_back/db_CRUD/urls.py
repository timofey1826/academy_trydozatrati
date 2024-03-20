from django.urls import path

from . import views, specific_commands

urlpatterns = [
    path("user/<id>",views.user_managing),
    path("get_job_title/<id>",views.job_title_managing),
    path("project/<id>",views.project_managing),
    path("task/<id>",views.task_managing),

    path("all_job_titles", specific_commands.get_all_job_titles),
    path("all_user_task/<user_id>", specific_commands.get_all_user_task),

    path('users/create',specific_commands.RegisterView.as_view()),#для регистрации пользователей
    path("users/login",specific_commands.LoginView.as_view()),#дяя входина
    path("users/auth",specific_commands.UserView.as_view()),
]