from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
