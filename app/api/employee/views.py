from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

# from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer, Employee_groupSerializer
from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer, Employee_groupSerializer
from app.api.position.serializers import PositionSerialzer
from app.model import Position, Employee, Group, Employee_group


class Employee_createAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class Employee_updateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class Employee_deleteAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'id'


class Employee_listAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = Employee_listSerializer
    queryset = Employee.objects.all()


class Employee_groupCreateapiView(CreateAPIView):
    serializer_class = Employee_groupSerializer
    queryset = Employee_group.objects.all()
# class Group_createAPIView(CreateAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
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
# class Group_deleteAPIView(DestroyAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#     lookup_url_kwarg = 'id'
#
# class Group_listAPIView(ListAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()

    # def get_queryset(self):
    #     id = self.request.data.get('id')
    #     u = Employee.objects.get(employee_id_id=id)
    #     if self.request.user.is_staff:
    #         if u == 'director':
    #             print()



