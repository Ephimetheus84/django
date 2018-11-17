from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=30)
    duration = models.TimeField(blank=True)

    def __str__(self):
        return self.name
