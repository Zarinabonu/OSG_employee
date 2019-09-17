from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    qr_code = models.TextField(null=True, blank=True)
    status = models.ForeignKey('Employee_status', on_delete=models.SET_NULL, null=True)


class Attendance(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    title = models.TextField(null=True, blank=True)
    deadline = models.DateField()


class Group(models.Model):
    group_name = models.CharField(max_length=100, null=True, blank=True)


class Employee_group(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    employee_group = models.ForeignKey('Group', on_delete=models.CASCADE)


class Employee_status(models.Model):
    status_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.IntegerField(null=True, blank=True)


