from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

# from app.api.employee.serializers import EmployeeSerializer
from app.model import Group
from rest_framework import serializers


class GroupSerializer(ModelSerializer):
    # creater = serializers.IntegerField(read_only=True)

    class Meta:
        model = Group
        fields = ('name',
                  'creater',
                  )

    # def create(self, validated_data):
    #     group = Group(**validated_data)
    #     request = self.context['request'].data.get('creater')
    #     group.creater = request
    #
    #     group.save()
    #     return group