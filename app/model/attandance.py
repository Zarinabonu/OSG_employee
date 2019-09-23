
from django.contrib.auth.models import User
from django.db import models


class Attendance(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
