from django.contrib import admin

from .model import Employee, Attendance, Job

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Job)
# Register your models here.
