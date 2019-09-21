from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField(null=True, blank=True)


class Employee_group(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    employee_group = models.ForeignKey('Group', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.user.username or 'asd'


