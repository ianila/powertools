from django.contrib.auth.models import User
from django.db import models

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

    def __str__(self):
        return self.user.profile.fullname
