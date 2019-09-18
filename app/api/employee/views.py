from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer, Employee_salarySerialzer
from app.api.status.serializers import StatusSerialzer
from app.model import Employee_status, Employee, Employee_salary


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

    # def get_queryset(self):
    #     id = self.request.data.get('id')
    #     u = Employee.objects.get(employee_id_id=id)
    #     if self.request.user.is_staff:
    #         if u == 'director':
    #             print()



class Employee_salaryAPIView(CreateAPIView):
    serializer_class = Employee_salarySerialzer
    queryset = Employee_salary.objects.all()


class Employee_salaryAPIView(CreateAPIView):
    serializer_class = Employee_salarySerialzer
    queryset = Employee_salary.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)