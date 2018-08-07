from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=False)
    nicno = models.CharField(max_length=10, blank=False)
    birth_date = models.DateField(null=True, blank=False)
    email = models.CharField(max_length=50, blank=True)

class Phone(models.Model):
    phoneno = models.CharField(max_length=10, blank=True)
    profile = models.ForeignKey(Profile)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
