from django.contrib.auth.models import User
from django.db import models

from app.models.employee import Employee
from app.models.group import Group


class Project(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name + 'task' + self.created

    class Meta:
        db_table = 'tasks'
