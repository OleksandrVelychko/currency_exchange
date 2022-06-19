from django.contrib import admin
from currency.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['__all__']
    search_fields = ['base_currency', 'currency', 'source']


admin.site.register(Currency, CurrencyAdmin)
