from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4, db_index=True, unique=True)
    conversion_rate = models.DecimalField(max_digits=8,
                                          decimal_places=5,
                                          default=0.0,
                                          help_text="Rate should equal 1 for base currency")
    base_currency = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    @classmethod
    def convert(cls, from_currency_code, to_currency_code, amount, user=None):
        from_curr = cls.objects.get(code=from_currency_code)
        to_curr = cls.objects.get(code=to_currency_code)
        converted_amount = round((amount * from_curr.conversion_rate)/to_curr.conversion_rate, 3)
        return converted_amount

    @classmethod
    def available_currencies(cls):
        return cls.objects.values_list('code', flat=True)
