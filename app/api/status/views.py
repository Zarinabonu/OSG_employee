from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView

from app.api.status.serializers import StatusSerialzer
from app.model import Employee_status


class Status_createAPIView(CreateAPIView):
    serializer_class = StatusSerialzer
    query_set = Employee_status.objects.all()


class Status_listAPIView(ListAPIView):
    serializer_class = StatusSerialzer
    query_set = Employee_status.objects.all()



