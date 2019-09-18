from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Job, Group, Employee_group, Employee
from rest_framework import serializers
from app.api.status.serializers import StatusSerialzer


class Job_Serializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('title',
                  'deadline',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        instance.save()

        return instance


class Job_listSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('title',
                  'deadline',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserSereializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')


class Employee_listSerializer(ModelSerializer):
    user = UserSereializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('image',
                  'status')


class Employee_groupSerialzier(ModelSerializer):
    employee_id = Employee_listSerializer
    class Meta:
        model = Employee_group
        fields = ('employee_id',
                  'employee_group')


class Group_Serialzier(ModelSerializer):
    employee_group = Employee_groupSerialzier(read_only=True)

    class Meta:
        model = Group
        fields = ('group_name',
                  'employee_group')

    def create(self, validated_data):
        group = Group(**validated_data)
        employees = self.context['request'].data.getlist('employee_id')
        group.save()

        for e in employees:
            # group.employee_group_set.add(Employee.objects.get(id=e))
            Employee_group.objects.create(employee_id_id=e, employee_group_id=group.id)

        return group

    def update(self, instance, validated_data):
        employees_add = self.context['request'].data.getlist('employee_add_id')
        employees_remove = self.context['request'].data.getlist('employee_remove_id')

        instance.group_name = self.context['request'].data.get('group_name')
        if employees_add:
            for e in employees_add:
                emplo = Employee_group.objects.create(employee_id_id=e, employee_group_id=instance.id)
        elif employees_remove:
            for e in employees_remove:
                emplo = Employee_group.objects.get(employee_id_id=e, employee_group_id=instance.id)
                emplo.delete()

        instance.save()
        return instance


class Group_listSerialzier(ModelSerializer):
    employee_group_set = Employee_groupSerialzier(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('group_name',
                  'employee_group_set')
