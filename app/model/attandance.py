
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Attendance(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    check_out = models.BooleanField(default=True)


@receiver(post_save, sender=Attendance)
def create_check_out(sender, instance, created, **kwargs):
    if created:
        request = instance.employee_id
        att = Attendance.objects.filter(employee_id=request)
        att = att.exclude(date_start=instance.date_start)
        attand = att.last_item()



