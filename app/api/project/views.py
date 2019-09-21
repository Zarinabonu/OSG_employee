from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer
# from app.api.project.serializers import  Group_listSerialzier, TaskSerialzer, Project_listSerializer
from app.api.position.serializers import PositionSerialzer
from app.model import Group, Employee_group, Employee, Task, Project




# class Task_createAPIView(CreateAPIView):
#     serializer_class = TaskSerialzer
#     queryset = Task.objects.all()
#
#
# class Task_deleteAPIView(DestroyAPIView):
#     serializer_class = TaskSerialzer
#     queryset = Task.objects.all()
#     lookup_url_kwarg = 'id'
#
#
# class Task_updateAPIView(UpdateAPIView):
#     serializer_class = TaskSerialzer
#     queryset = Task.objects.all()
#     lookup_url_kwarg = 'id'
#
#
# class Project_listAPIView(ListAPIView):
#     serializer_class = Project_listSerializer
#     queryset = Project.objects.all()
