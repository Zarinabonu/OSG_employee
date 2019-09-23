from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

from app.api.employee.serializers import Group_listSerialzier, Employee_listSerializer
from app.api.group.serializers import GroupSerializer
from app.model import Group, Employee_group, Employee, Project, Task
from rest_framework import serializers
from app.api.position.serializers import PositionSerialzer

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
#
#
class Project_Serialzer(ModelSerializer):
    group_id = GroupSerializer(read_only=True)
    group_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Project
        fields = ('title',
                  'description',
                  'deadline',
                  'group_id',
                  'group_id_id')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class Project_listSerializer(ModelSerializer):
    group_id = GroupSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('title',
                  'description',
                  'deadline',
                  'group_id')


class TaskSerialzer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('task',)

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        p = self.context['request'].data.get('project_id')
        project = Project.objects.get(id=p)
        task.project_id = project
        employee_id = self.context['request'].data.get('employee_id')
        if employee_id:
            task.employee_id_id = employee_id
            task.save()

        return task

    def update(self, instance, validated_data):
        employee = self.context['request'].data.get('employee_id')
        if employee:
            instance.employee_id = employee

        instance.save()
        return instance


class Task_listSerializer(ModelSerializer):
    employee_id = Employee_listSerializer(read_only=True)
    project_id = Project_listSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('task',
                  'employee_id',
                  'project_id')







