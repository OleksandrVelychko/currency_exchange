from django.contrib.auth.models import User
from django.views.generic import CreateView

from accounts.forms import AccountRegisterForm


class AccountRegister(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = AccountRegisterForm
