from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer
from app.api.project.serializers import Job_Serializer, Job_listSerializer, Group_Serialzier, Group_listSerialzier
from app.api.status.serializers import StatusSerialzer
from app.model import Job, Group, Employee_group, Employee


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


class Project_deleteAPIView(DestroyAPIView):
    serializer_class = Job_Serializer
    queryset = Job.objects.all()
    lookup_url_kwarg = 'id'


class Project_listAPIView(ListAPIView):
    serializer_class = Job_listSerializer
    queryset = Job.objects.all()


class Group_createAPIView(CreateAPIView):
    serializer_class = Group_Serialzier
    queryset = Group.objects.all()


class Group_updateAPIView(UpdateAPIView):
    serializer_class = Group_Serialzier
    queryset = Group.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)



class Group_deleteAPIView(DestroyAPIView):
    serializer_class = Group_Serialzier
    queryset = Group.objects.all()
    lookup_url_kwarg = 'id'


class Group_listAPIView(ListAPIView):
    serializer_class = Group_listSerialzier
    queryset = Group.objects.all()

