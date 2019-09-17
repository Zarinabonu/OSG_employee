from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer
from app.api.project.serializers import Job_Serializer
from app.api.status.serializers import StatusSerialzer
from app.model import Job, Group, Employee_group


class Project_createAPIView(CreateAPIView):
    serializer_class = Job_Serializer
    queryset = Job.objects.all()


class Project_updateAPIView(CreateAPIView):
    serializer_class = Job_Serializer
    queryset = Job.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


