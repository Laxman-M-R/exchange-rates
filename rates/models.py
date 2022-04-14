from django.db import models
from django.utils import timezone

# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=8, blank=True, null=True, unique=True)
    full_name = models.CharField(max_length=256, blank=True, null=True)

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency,
                                             on_delete=models.CASCADE, 
                                             blank=True, 
                                             null=True, 
                                             related_name='base_currency')
    target_currency = models.ForeignKey(Currency,
                                                   on_delete=models.CASCADE, 
                                                   blank=True, 
                                                   null=True, 
                                                   related_name='target_currency')
    exchange_rate = models.FloatField(default=1.0)
    exchange_rate_date = models.DateField(default=timezone.now)

