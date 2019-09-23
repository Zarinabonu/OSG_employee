from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.accountant.serializers import AccountantSerializer, Accountant_listSerialzier
from app.api.attendance.serializers import AttandanceSerialzier
from app.model import Accountant
from datetime import datetime


class Accountant_createAPIView(CreateAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()


class Accountant_updateAPIView(UpdateAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()
    lookup_url_kwarg = 'id'


class Accountant_deleteAPIView(DestroyAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()
    lookup_url_kwarg = 'id'


class Accountant_listAPIView(ListAPIView):
    serializer_class = Accountant_listSerialzier
    queryset = Accountant.objects.all()
    print('l')