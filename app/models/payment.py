from datetime import timezone

from django.db import models

from app.model.employee import Employee


class Payment(models.Model):
    date = models.DateTimeField(default=timezone.now())
    summ = models.IntegerField(default=0, null=True, blank=True)
    employee = models.ForeignKey(Employee, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date.month

    class Meta:
        db_table = 'payments'