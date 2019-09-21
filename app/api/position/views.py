from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView

from app.api.position.serializers import PositionSerialzer
from app.model import Position


class Position_createAPIView(CreateAPIView):
    serializer_class = PositionSerialzer
    query_set = Position.objects.all()


class Position_listAPIView(ListAPIView):
    serializer_class = PositionSerialzer
    query_set = Position.objects.all()



