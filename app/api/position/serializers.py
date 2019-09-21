# position serializerini shu yerga yozing



from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.models import Position
from rest_framework import serializers


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ('name',
                  'access_level')

    def create(self, validated_data):
        status = Position(**validated_data)
        request = self.context['request']
        if status.name == 'Director':
            status.access_level = '5'
        elif status.name == 'Project meneger':
            status.access_level = '4'
        elif status.name == 'Programmer':
            status.access_level = '3'
        else:
            status.access_level = '0'
        status.save()
        return status