from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.attendance.serializers import AttandanceSerialzier
from app.model import Attendance, Employee
from datetime import datetime


class Attandance_createAPIView(APIView):
    serializer_class = AttandanceSerialzier
    queryset = Attendance.objects.all()

    def post(self, request):
        q_code = request.POST.get('qr_code')
        e = Employee.objects.get(register_num=q_code)
        if e.attendance_set.filter(created=datetime.now().date()).count()>0:
            e_finish = e.attendance_set.get(created=datetime.now().date())
            e_finish.date_finish = datetime.now()
            e_finish.save()
        else:
            a = Attendance.objects.create(employee_id=e)

        print(e.attendance_set.filter(created=datetime.now().date()).count())
        #     pass
        return Response(status=200)
