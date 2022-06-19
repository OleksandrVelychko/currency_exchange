from django.contrib.auth.models import User
from django.views.generic import CreateView


class AccountRegister(CreateView):
    model = User
    template_name = 'accounts/register.html'
