from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import *
from .models import *
from django.urls import reverse_lazy,reverse
from typing import Any
from user.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy,reverse

# project create

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'
    
class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "project/project_detail.html"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/project_delete.html"    
    success_url = "/project/list/"

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = "/project/list/"
    template_name = "project/project_update_form.html" 

# project team

class ProjectTeamCreateView(CreateView):    
    template_name = 'project/create_team.html'
    model = ProjectTeam
    success_url = '/project/list_team/'
    form_class = ProjectTeamCreationForm 

class ProjectTeamUpdateView(UpdateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm 
    success_url = "/project/list/"
    template_name = "project/update_team.html"

class ProjectTeamView(ListView):
    template_name = 'project/team_view.html'
    model = Project
    context_object_name = 'projects'

class ProjectTeamDeleteView(DeleteView):
    model = ProjectTeam
    template_name = "project/project_team_delete.html"    
    success_url = "/project/list_team/"


# project Module


class ProjectModuleCreationView(CreateView):
    template_name = 'project/create_module.html'
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    success_url = '/project/list_module/' 
    # def get_success_url(self) -> str:
    #     success_url=reverse_lazy('module_list/',kwargs={'pk':self.kwargs['id']})
    #     return success_url  

class ProjectModuleDetailView(DetailView):
    model = ProjectModule
    context_object_name = "modules"
    template_name = "project/module_detail.html"

class ProjectModuleListView(ListView):
    template_name = 'project/module_list.html'
    model = ProjectModule
    context_object_name = 'modules'


class ProjectModuleUpdateView(UpdateView):
    model = ProjectModule
    form_class = ProjectModuleCreationForm 
    success_url = "/project/list_module/"
    template_name = "project/update_module.html"

class ProjectModuleDeleteView(DeleteView):
    model = ProjectModule
    template_name = "project/project_module_delete.html"    
    success_url = "/project/list_module/"


# project Task

class ProjectTaskCreationView(CreateView):
    model=Task
    form_class=ProjectTaskCreationForm
    template_name='project/create_task.html'
    # success_url="/project/list_task/"
    def get_success_url(self):
        success_url=reverse_lazy('showmodule',kwargs={'pk':self.kwargs['id']})
        return success_url

class ProjectTaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "project/task_detail.html"

class ProjectTaskListView(ListView):
    template_name = 'project/task_list.html'
    model = Task
    context_object_name = 'task'

class ProjectTaskUpdateView(UpdateView):
    model = Task
    form_class = ProjectTaskCreationForm 
    success_url = "/project/list_task/"
    template_name = "project/update_task.html"

class ProjectTaskDeleteView(DeleteView):
    model = Task
    template_name = "project/project_task_delete.html"    
    success_url = "/project/list_task/"


# Project Status


class ProjectStatusCreationView(CreateView):
    model=Status
    form_class=ProjectStatusCreationForm
    template_name='project/create_status.html'
    success_url='/user/manager-dashboard/'


    


# class ProjectStatusDetailView(DetailView):
#     model = Status
#     context_object_name = "status"
#     template_name = "project/status_detail.html"

# class ProjectStatusListView(ListView):
#     template_name = 'project/status_list.html'
#     model = Status
#     context_object_name = 'status'

# class ProjectStatusUpdateView(UpdateView):
#     model = Status
#     form_class = ProjectStatusCreationForm 
#     success_url = "/project/list_status/"
#     template_name = "project/update_status.html"

# class ProjectStatusDeleteView(DeleteView):
#     model = Status
#     template_name = "project/project_status_delete.html"    
#     success_url = "/project/list_status/"



# class DeveloperDetailView(DetailView):
#     model=User
#     context_object_name='developer'
#     template_name='user/developer_detail.html'



