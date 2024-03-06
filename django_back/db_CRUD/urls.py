from django.urls import path

from . import views, specific_commands
from .views import TokenObtainPairViewModified

urlpatterns = [
    path("user/<id>",views.user_managing),
    path("get_job_title/<id>",views.job_title_managing),
    path("project/<id>",views.project_managing),
    path("task/<id>",views.task_managing),

    path("all_task", specific_commands.get_all_tasks),
    path("all_user_task/<user_id>", specific_commands.get_all_user_task),
    path('token/', TokenObtainPairViewModified.as_view(), name='token_obtain_pair')
]