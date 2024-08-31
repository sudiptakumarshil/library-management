from django import forms
from .models import Transections


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transections
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop("account")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.account = self.account
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f"You need to deposit at least {min_deposit_amount} $"
            )

        return amount
