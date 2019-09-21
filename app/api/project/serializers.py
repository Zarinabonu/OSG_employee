# from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
# from django.contrib.auth.models import User
#
# from app.api.employee.serializers import Group_listSerialzier
# from app.model import Group, Employee_group, Employee, Project, Task
# from rest_framework import serializers
# from app.api.position.serializers import PositionSerialzer
#
#
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
# class Employee_groupSerializer(ModelSerializer):
#     employee_id = Employee_listSerializer(read_only=True)
#
#     class Meta:
#         model = Employee_group
#         fields = ('employee_id',
#                   'employee_group')
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





