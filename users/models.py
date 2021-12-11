from django.db import models
from django.contrib.auth.models import AbstractUser

from orders.models import Order


class CustomUser(AbstractUser):
    birth_date = models.DateField(max_length=16, blank=True, null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='product',
        blank=True,
        null=True
    )
