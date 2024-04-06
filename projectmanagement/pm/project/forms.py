from django import forms
from .models import *


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'})
        }

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields ='__all__' 

class ProjectModuleCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'})
        }

class ProjectStatusCreationForm(forms.ModelForm):
    class Meta:
        model=Status
        fields="__all__"

class ProjectTaskCreationForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"     
        
        
        
        