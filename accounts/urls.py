from django.urls import path
from accounts.views import AccountRegister

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
]
