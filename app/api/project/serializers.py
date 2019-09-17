from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Job, Group, Employee_group
from rest_framework import serializers
from app.api.status.serializers import StatusSerialzer


class Job_Serializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('title',
                  'deadline')

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
                  'deadline')

