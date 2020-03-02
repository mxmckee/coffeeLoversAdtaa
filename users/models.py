from django.db import models
from django.contrib.auth.models import AbstractUser

class AdtaaUser(AbstractUser):
    ACCESS_CHOICES=(
        ('RU', 'Root User'),
        ('AU', 'Admin User'),
        ('SU', 'Scheduler User'),
        ('', '--------'),
    )

    accessRequested = models.CharField(
        max_length=2,
        choices=ACCESS_CHOICES,
        default='',
        blank=True,
    )

    is_active = models.BooleanField(
        default=False
    )

