from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name='profile'
    )
