from django.db import models

from .cinema import Cinema


class Hall(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
