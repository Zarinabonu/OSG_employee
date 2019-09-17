from django.contrib import admin

from .model import Employee, Attendance, Job, Employee_group, Group, Employee_status

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Job)
admin.site.register(Employee_group)
admin.site.register(Group)
admin.site.register(Employee_status)
# Register your models here.
