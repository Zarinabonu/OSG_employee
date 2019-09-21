from django.contrib import admin

from .model import Employee, Attendance, Employee_group, Group, Position, Task, Project


admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Employee_group)
admin.site.register(Group)
admin.site.register(Position)
admin.site.register(Task)
admin.site.register(Project)
# Register your models here.
