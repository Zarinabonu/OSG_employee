from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    access_level = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'positions'