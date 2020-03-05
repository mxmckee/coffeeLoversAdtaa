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
        default=True
    )

class Profile(models.Model):
    user = models.OneToOneField(AdtaaUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

