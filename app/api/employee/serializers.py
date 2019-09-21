# Employee va EmployeeGroup serializerlarini shu yerga yozing
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
#
from rest_framework import serializers
#
#
#
from app.api.position.serializers import PositionSerializer
from app.models import Employee, EmployeeGroup, Group


class EmployeeSerializer(ModelSerializer):
    position = PositionSerializer(read_only=True)
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
                  'position_id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'password',
                  )

    def create(self, validated_data):
        username = validated_data.pop('username')
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')
        is_active = validated_data.pop('is_active')
        password = validated_data.pop('password')

        employee = Employee(**validated_data)
        u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email, is_active=is_active)
        u.set_password(password)
        u.save()
        employee.user = u

        employee.save()
        return employee

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        print('hello', instance)

        if validated_data.get('password'):
            p = validated_data.pop('password'   )
            instance.user.set_password(p)
        for attr, value in validated_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        instance.save()

        return instance


class Employee_userlistSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')


class Group_Serialzier(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class Employee_groupSerialzier(ModelSerializer):
    employee_group = Group_Serialzier()

    class Meta:
        model = EmployeeGroup
        fields = ('employee_group',)


class Employee_listSerializer(ModelSerializer):
    user = Employee_userlistSerializer()
    employee_group_set = Employee_groupSerialzier(many=True, read_only=True)
    position = PositionSerializer(read_only=True)

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
        print(instance.employee_salary.id)
        position_e = super(Employee_listSerializer, self).to_representation(instance)
        print('111', position_e)
        if instance.name.degree == 9:
            position_e.pop('salary')
        elif instance.name.degree == 8:
            position_e.pop('employee_group_set')
            position_e.pop('salary')

        elif instance.name.degree == 7:
            position_e.pop('employee_group_set')
        elif instance.name.degree == 6:
            position_e.pop('address')
            position_e.pop('image')
            position_e.pop('phone')
            position_e.pop('salary')
            position_e.pop('user')
            position_e.pop('employee_group_set')


        return position_e
