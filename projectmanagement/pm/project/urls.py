from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("detail/<int:pk>/",ProjectDetailView.as_view(),name="detail_project"),
 path("delete/<int:pk>/",ProjectDeleteView.as_view(),name="delete_project"),
 path("update/<int:pk>/",ProjectUpdateView.as_view(),name="update_project"),


 path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
 path("update_team/<int:pk>/",ProjectTeamUpdateView.as_view(),name="project_team_update"),
 path("list_team/",ProjectTeamView.as_view(),name="project_team_list"),


 path("create_module/",ProjectModuleCreationView.as_view(),name="project_module_create"),
 path("list_module/",ProjectModuleListView.as_view(),name="project_module_list"),
 path("detail_module/<int:pk>/",ProjectModuleDetailView.as_view(),name="detail_module_project"),
 path("delete_module/<int:pk>/",ProjectModuleDeleteView.as_view(),name="delete_module_project"),
 path("update_module/<int:pk>/",ProjectModuleUpdateView.as_view(),name="update_module_project"),


 path("create_task/",ProjectTaskCreationView.as_view(),name="project_task_create"),
 path("list_task/",ProjectTaskListView.as_view(),name="project_task_list"),
 path("detail_task/<int:pk>/",ProjectTaskDetailView.as_view(),name="detail_task_project"),
 path("delete_task/<int:pk>/",ProjectTaskDeleteView.as_view(),name="delete_task_project"),
 path("update_task/<int:pk>/",ProjectTaskUpdateView.as_view(),name="update_task_project"),


path("create_status/",ProjectStatusCreationView.as_view(),name="project_status_create"),

]