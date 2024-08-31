from django.db import models
from user.models import UserAccount


class Transections(models.Model):
    account = models.ForeignKey(
        UserAccount, related_name="transactions", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
