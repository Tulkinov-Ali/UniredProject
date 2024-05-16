from django.db import models


# Model for saving new currency or old one will be updated
class CurrencyExchangeRate(models.Model):
    _id = models.BigIntegerField()
    code = models.CharField(max_length=10)
    ccy = models.CharField(max_length=10)
    ccynm_en = models.CharField(max_length=100)
    ccynm_uz = models.CharField(max_length=100)
    ccynm_uzc = models.CharField(max_length=100)
    ccynm_ru = models.CharField(max_length=100)
    rate = models.FloatField()
    diff = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'{self.ccy} - {self.date}'
