from django.db import models

# Create your models here.
class Referral():
    folio = models.CharField(max_length=50, blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    tax = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=15, default=0)