# Project va task serializerlarini shu yerga yozing


# from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
# from django.contrib.auth.models import User
# from app.model import Group, Employee_group, Employee, Project, Task
# from rest_framework import serializers
# from app.api.status.serializers import StatusSerialzer
#
#
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')
#
#
# class UserSereializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('last_name', 'first_name')
#
#
# class Employee_listSerializer(ModelSerializer):
#     user = UserSereializer(read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ('image',
#                   'status',
#                   'user')
#
#
# class Employee_groupSerialzier(ModelSerializer):
#     employee_id = Employee_listSerializer(read_only=True)
#
#     class Meta:
#         model = Employee_group
#         fields = ('employee_id',
#                   'employee_group')
#
#
# class Group_Serialzier(ModelSerializer):
#     employee_group = Employee_groupSerialzier(read_only=True)
#
#     class Meta:
#         model = Group
#         fields = ('group_name',
#                   'employee_group')
#
#     def create(self, validated_data):
#         group = Group(**validated_data)
#         employees = self.context['request'].data.getlist('employee_id')
#         group.save()
#
#         p_id = self.context['request'].data.get('project_id')
#         p_deadline = self.context['request'].data.get('deadline')
#         p = Project.objects.get(id=p_id)
#         p.group_id = group
#         p.deadline = p_deadline
#         for e in employees:
#             # group.employee_group_set.add(Employee.objects.get(id=e))
#             Employee_group.objects.create(employee_id_id=e, employee_group_id=group.id)
#
#         return group
#
#     def update(self, instance, validated_data):
#         employees_add = self.context['request'].data.getlist('employee_add_id')
#         employees_remove = self.context['request'].data.getlist('employee_remove_id')
#
#         instance.group_name = self.context['request'].data.get('group_name')
#         if employees_add:
#             for e in employees_add:
#                 emplo = Employee_group.objects.create(employee_id_id=e, employee_group_id=instance.id)
#         elif employees_remove:
#             for e in employees_remove:
#                 emplo = Employee_group.objects.get(employee_id_id=e, employee_group_id=instance.id)
#                 emplo.delete()
#
#         instance.save()
#         return instance
#
#
# class Group_listSerialzier(ModelSerializer):
#     employee_group_set = Employee_groupSerialzier(many=True, read_only=True)
#
#     class Meta:
#         model = Group
#         fields = ('group_name',
#                   'employee_group_set')
#
#
# class TaskSerialzer(ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('task',)
#
#     def create(self, validated_data):
#         task = Task(**validated_data)
#         task.save()
#         p = self.context['request'].data.get('project_id')
#         project = Project.objects.get(id=p)
#         task.project_id = project
#         employee_id = self.context['request'].data.get('employee_id')
#         if employee_id:
#             task.employee_id = employee_id
#         task.save()
#
#     def update(self, instance, validated_data):
#         instance.task = self.context['request'].data.getlist('task')
#         employee = self.context['request'].data.get('employee_id')
#         if employee:
#             instance.employee_id = employee
#
#         instance.save()
#         return instance
#
#
# class Project_Serialzer(ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('title',
#                   'description',
#                   'deadline')
#
#     def update(self, instance, validated_data):
#         instance.title = self.context['request'].data.getlist('title')
#         instance.description = self.context['request'].data.getlist('description')
#         instance.deadline = self.context['request'].data.getlist('deadline')
#
#         instance.save()
#         return instance
#
#
# class Project_listSerializer(ModelSerializer):
#     group_id = Group_listSerialzier(read_only=True)
#
#     class Meta:
#         model = Project
#         fields = ('title',
#                   'description',
#                   'deadline',
#                   'group_id')
#
#
#
#
#
#
#
#
