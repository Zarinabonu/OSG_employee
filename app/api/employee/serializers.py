from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

# from app.api.project.serializers import Employee_groupSerializer
from app.api.group.serializers import GroupSerializer
from app.api.user.serializers import UserSerialzier
from app.model import Employee, Employee_group, Group, Project
from rest_framework import serializers
from app.api.position.serializers import PositionSerialzer


class EmployeeSerializer(ModelSerializer):
    position = PositionSerialzer(read_only=True)
    position_id = serializers.IntegerField(write_only=True)
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    is_active = serializers.BooleanField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('image',
                  'phone',
                  'address',
                  'position',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'salary',
                  'is_active',
                  'password',
                  'position_id',
                  )

    def create(self, validated_data):
        username = validated_data.pop('username')
        #     _id = serializers.IntegerField(write_only=True)
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')
        is_active = validated_data.pop('is_active')
        password = validated_data.pop('password')

        employee = Employee(**validated_data)
        u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email,
                                is_active=is_active)
        u.set_password(password)
        u.save()
        employee.user = u
        employee.save()
        return employee

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('password'):
            p = validated_data.pop('password')
            instance.user.set_password(p)
        for attr, value in validated_data.items():
            setattr(instance.user, attr, value)
            setattr(instance, attr, value)

        instance.user.save()
        instance.save()

        return instance


class Group_Serialzier(ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name',)


class Employee_groupSerialzier(ModelSerializer):
    employee_group = Group_Serialzier()

    class Meta:
        model = Employee_group
        fields = ('employee_group',)


class Employee_listSerializer(ModelSerializer):
    user = UserSerialzier()
    employee_group_set = Employee_groupSerialzier(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('image',
                  'phone',
                  'address',
                  'position',
                  'user',
                  'salary',
                  'employee_group_set')

    def to_representation(self, instance):
        employee_status = super(Employee_listSerializer, self).to_representation(instance)
        print('111', instance.position.degree)
        if instance.position.degree == 9:
            employee_status.pop('salary')
        elif instance.position.degree == 8:
            employee_status.pop('salary')
            employee_status.pop('employee_group_set')

        elif instance.position.degree == 7:
            employee_status.pop('employee_group_set')
        elif instance.position.degree == 6:
            employee_status.pop('image',
                                'phone',
                                'address',
                                'position',
                                'user',
                                'salary',
                                'employee_group_set')

        return employee_status


class Employee_groupSerializer(ModelSerializer):
    employee_group = GroupSerializer(read_only=True)
    employee_id = EmployeeSerializer(read_only=True)
    employee_id_id = serializers.IntegerField(write_only=True)
    employee_group_id = serializers.IntegerField(write_only=True)

    # employee_id = EmployeeSerializer(read_only=True)

    class Meta:
        model = Employee_group
        fields = ('employee_group',
                  'employee_id',
                  'employee_group_id',
                  'employee_id_id',
                  )

    # def create(self, validated_data):
    #     group_name = validated_data.pop('employee_group')['name']
    #     creater = validated_data.pop('employee_group')['creater']
    #     group = Group.objects.create(name=group_name, creater=creater)
    #     employee_g = Employee_group.objects.create(employee_group=group, employee_id=1)
    #     print('132', employee_g)

        # e_group = self.context['request'].data.getlist('employee_id')
        # # e_group = Employee.objects.get(id=employees)
        # for e in e_group:
        #     employee_g.employee_id = e
        #     employee_g.save()

        # return employee_gs

    # def create(self, validated_data):
    #     employee_group = Employee_group(**validated_data)

# class Group_Serialzier(ModelSerializer):
#     employee_group = Employee_groupSerializer(read_only=True)
#
#     class Meta:
#         model = Group
#         fields = ('name',
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
#         fields = ('name',
#                   'employee_group_set')
