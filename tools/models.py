from django.db import models

class Tool(models.Model):
    serialno = models.CharField(max_length=16, blank=False, null=False)
    last_rentered = models.DateTimeField(blank=False, null=False)
    make = models.CharField(max_length=16, blank=False, null=False)
    rentalvalue = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(blank=True, null=True)
