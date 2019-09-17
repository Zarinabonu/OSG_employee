from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Employee_status
from rest_framework import serializers


class StatusSerialzer(ModelSerializer):
    class Meta:
        model = Employee_status
        fields = ('status_name',
                  'degree')

    # def create(self, validated_data):
    #     status = Employee_status(**validated_data)
    #     request = self.context['request']
    #     if status.status_name == 'Director':
    #         status.degree = '5'
    #     elif status.status_name == 'Project meneger':
    #         status.degree = '4'
    #     elif status.status_name == 'Programmer':
    #         status.degree = '3'
    #     else:
    #         status.degree = '0'
    #     status.save()
    #     return status