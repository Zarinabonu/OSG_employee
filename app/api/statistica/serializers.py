from rest_framework.serializers import Serializer, ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

from app.api.user.serializers import UserSerilizer
from app.model import Group, Employee, Attendance, Accountant, Employee_salary, Project
from rest_framework import serializers


class StaticSerializer(ModelSerializer):
    # employee_id = EmployeeSerializer(read_only=True)
    # employee_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Attendance
        fields = ('date_start',
                  'date_finish')


class E_static(ModelSerializer):
    user = UserSerilizer(read_only=True)
    attendance_set = StaticSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'attendance_set',
                  )


class GiveMSerializer(ModelSerializer):

    class Meta:
        model = Accountant
        fields = ('id',
                  'sum',
                  'date',
                  'date')


class GiveMoneySerializer(ModelSerializer):
    user = UserSerilizer(read_only=True)
    accountant_set = GiveMSerializer(many=True, read_only=True, source='accounter_id')

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'accountant_set',
                  )


class Salary(ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = ('id',
                  'sum',
                  'date')


class SalarySerializer(ModelSerializer):
    user = UserSerilizer(read_only=True)
    employee_salary_set = Salary(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'employee_salary_set',
                  )


class projectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'deadline',
                  'done_date')


class ProjectSerializer(ModelSerializer):
    user = UserSerilizer(read_only=True)
    project = serializers.SerializerMethodField()
    doneproject = serializers.SerializerMethodField()


    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'project',
                  'doneproject'
                  )

    def get_project(self, obj):
        qs = Project.objects.filter(group_id__employee_group__employee_id=obj).filter(done=False)
        return projectSerializer(qs, many=True, context=self.context).data

    def get_doneproject(self, obj):
        qs = Project.objects.filter(group_id__employee_group__employee_id=obj).filter(done=True)
        return projectSerializer(qs, many=True, context=self.context).data


class StaticsSerializer(Serializer):
    att = serializers.SerializerMethodField()
    givenMoney = serializers.SerializerMethodField()
    salary = serializers.SerializerMethodField()
    active_project = serializers.SerializerMethodField()

    def get_att(self, obj):
        qs = Employee.objects.all()
        return E_static(qs, many=True, context=self.context).data

    def get_givenMoney(self, obj):
        qs = Employee.objects.all()
        return GiveMoneySerializer(qs, many=True, context=self.context).data

    def get_salary(self, obj):
        qs = Employee.objects.all()
        return SalarySerializer(qs, many=True, context=self.context).data

    def get_active_project(self, obj):
        qs = Employee.objects.all()
        return ProjectSerializer(qs, many=True, context=self.context).data





