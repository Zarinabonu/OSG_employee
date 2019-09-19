from django.contrib import admin

from .model import Employee, Attendance, Employee_group, Group, Employee_status, Employee_salary, Task, Project


admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Employee_group)
admin.site.register(Group)
admin.site.register(Employee_status)
admin.site.register(Employee_salary)
admin.site.register(Task)
admin.site.register(Project)
# Register your models here.
