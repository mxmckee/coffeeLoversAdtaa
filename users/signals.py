from django.db.models.signals import post_save
from .models import AdtaaUser, Profile
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=AdtaaUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AdtaaUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=AdtaaUser)
# def send_email_to_root(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             'User {} has been created'.format(instance.username),
#             'A new user has been created.  Access requested: {}'.format(instance.accessRequested),
#             'clarklander1983@gmail.com',
#             ['clarklander1983@gmail.com'],
#             fail_silently=False,
#
#         )