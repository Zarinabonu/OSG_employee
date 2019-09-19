from django.contrib.auth.models import User
from django.db import models
from app.model.user import Employee_group, Employee, Group


class Project(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)


class Task(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    task = models.TextField(null=True, blank=True)