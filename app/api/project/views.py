# Project va task viewlarini shu yerga yozing

# from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
#
# from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer
# from app.api.project.serializers import Group_Serialzier, Group_listSerialzier, TaskSerialzer, Project_listSerializer
# from app.api.status.serializers import StatusSerialzer
# from app.model import Group, Employee_group, Employee, Task, Project
#
#
# class Group_createAPIView(CreateAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#
#
# class Group_updateAPIView(UpdateAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#     lookup_url_kwarg = 'id'
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
#
#
#
# class Group_deleteAPIView(DestroyAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#     lookup_url_kwarg = 'id'
#
#
# class Group_listAPIView(ListAPIView):
#     serializer_class = Group_listSerialzier
#     queryset = Group.objects.all()
#
#
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
