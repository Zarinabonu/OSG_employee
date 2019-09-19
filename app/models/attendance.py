from django.db import models

from app.model.employee import Employee


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.user.username + ' attendance'

    class Meta:
        db_table = 'attendances'
