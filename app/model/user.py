from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    qr_code = models.TextField(null=True, blank=True)
    finger_print = models.ImageField(null=True, blank=True)
    scaner = models.ImageField(null=True, blank=True)


class Attendance(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(auto_now_add=True)


