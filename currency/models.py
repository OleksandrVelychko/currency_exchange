from django.db import models


class Source(models.Model):
    class SourceCodeName(models.IntegerChoices):
        PRIVATBANK = 1, 'PrivatBank'
        MONOBANK = 2, 'MonoBank'

    name = models.CharField(max_length=64, unique=True)
    code_name = models.PositiveSmallIntegerField(
        default=None,
        choices=SourceCodeName.choices,
        unique=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    class CurrencyType(models.TextChoices):
        UAH = 'UAH', 'Hryvnia'
        USD = 'USD', 'US Dollar'
        EUR = 'EUR', 'Euro'
        GBP = 'GBP', 'British Pound'
        CAD = 'CAD', 'Canadian Dollar'

    base_currency = models.CharField(max_length=5,
                                     choices=CurrencyType.choices,
                                     default=CurrencyType.UAH)
    currency = models.CharField(max_length=5, choices=CurrencyType.choices)
    saleRate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    purchaseRate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Nbu_Rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='rates')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
