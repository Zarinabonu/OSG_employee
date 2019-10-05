from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

# from app.api.employee.serializers import Employee_salarySerializer
from app.api.group.serializers import Employee_groupSerializer
from app.api.salary.serializers import Employee_salarySerializer
from app.api.position.serializers import PositionSerialzer
from app.model import Position, Employee
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name',
                  'first_name',
                  'username',
                  'email',
                  )


class Employee_infoSerializer(ModelSerializer):
    position = PositionSerialzer(read_only=True)
    employee_salary_set = Employee_salarySerializer(read_only=True, many=True)
    employee_group_set = Employee_groupSerializer()

    class Meta:
        model = Employee
        fields = ('user',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  'employee_salary_set',
                  'employee_group_set',
                  )