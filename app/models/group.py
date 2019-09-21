from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or 'asd'

    class Meta:
        db_table = 'groups'