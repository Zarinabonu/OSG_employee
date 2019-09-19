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



class Group(models.Model):
    group_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.group_name or 'asd'


class Employee_group(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    employee_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_id.user.username or 'asd'


class Employee_status(models.Model):
    status_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.status_name


class Employee_salary(models.Model):
    employee_id = models.OneToOneField('Employee', on_delete=models.CASCADE)
    salary = models.IntegerField()

