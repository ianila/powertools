from django.db import models

class Tool(models.Model):
    serialno = models.CharField(max_length=16, blank=False, null=False)
    last_rentered = models.DateTimeField(blank=False, null=False)
    make = models.CharField(max_length=16, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
