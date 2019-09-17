from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Employee
from rest_framework import serializers
from app.api.status.serializers import StatusSerialzer


class EmployeeSerializer(ModelSerializer):
    status = StatusSerialzer(read_only=True)
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
                  'status',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'password',
                  )

    def create(self, validated_data):
        username = validated_data.pop('username')
    #     _id = serializers.IntegerField(write_only=True)
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')
        is_active = validated_data.pop('is_active')
        password = validated_data('password')
    #
        employee = Employee(**validated_data)
        u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email, is_active=is_active)
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


class Employee_listSerializer(ModelSerializer):
    user = Employee_userlistSerializer()

    class Meta:
        model = Employee
        fields = ('image',
                  'phone',
                  'address',
                  'status',
                  'user')





