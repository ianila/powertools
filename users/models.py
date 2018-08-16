from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = (
        ('ROOTUSER', 'Root User'),
        ('STAFF', 'Staff'),
        ('CUSTOMER', 'Customer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    fullname = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    nic = models.CharField(max_length=10, blank=True)
    mobilephone = models.CharField(max_length=10, blank=True)
    homephone = models.CharField(max_length=10, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
