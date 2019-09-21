from django.contrib.auth.models import User
from django.db import models

from app.models.group import Group
from app.models.position import Position


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    register_number = models.TextField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.user.username + ' employee'


class EmployeeGroup(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.user.username + ' ' + self.group.name +  ' group'

    class Meta:
        db_table = 'employee_groups'