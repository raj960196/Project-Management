from django.db import models
from user.models import User
# from .g import GoogleCalendarField

# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
     
    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name 

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"

    def __str__(self):
        return self.user.username

class Status(models.Model):
    status = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length = 100,null=True)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name
    
sta = (
       ('start','start'),
       ('In Progress','In Progress'),
       ('Complate','complate'),
       )

class ProjectModule(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    module_name = models.CharField(max_length = 30,null=False)
    des = models.CharField(max_length = 30,null=True)
    estimated_hours = models.PositiveIntegerField()
    status = models.CharField(max_length=100,choices=sta)
    #  technology = models.CharField(max_length=100,choices=techChoices)
    startDate = models.DateField()

    class Meta:
        db_table = 'projectmodule'

    def __str__(self):
        return self.module_name

class Task(models.Model):
    module_id = models.ForeignKey(ProjectModule,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    tital = models.CharField(max_length = 100)
    priority = models.CharField(max_length=100)
    des = models.CharField(max_length = 300,null = False)
    status_id = models.ForeignKey(Status,on_delete=models.CASCADE)
    total_minute = models.IntegerField()

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.tital

class UserTask(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task,on_delete = models.CASCADE)

    class Meta:
        db_table = 'usertask'
    

    