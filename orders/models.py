from django.db import models
from django.utils import timezone


class Order(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.pk} - {self.title} - {self.creation_date}'
