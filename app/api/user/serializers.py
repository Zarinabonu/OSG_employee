from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Position
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerialzier(ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name',
                  'first_name',
                  'username',
                  'email',
                  'password')