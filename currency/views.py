from django.views.generic import ListView
# from currency.forms import CurrencyFilter # noqa
from currency.models import Currency


class CurrencyListView(ListView):
    model = Currency
    template_name = 'currency/list_currency.html'
