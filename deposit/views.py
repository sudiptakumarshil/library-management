from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import DepositForm
from deposit.models import Transections
from django.db import transaction, DatabaseError


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = "deposit.html"
    model = Transections
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"

    def form_valid(self, form):
        try:
            with transaction.atomic():
                amount = form.cleaned_data.get("amount")
                account = self.request.user.account
                account.balance += amount
                account.save(update_fields=["balance"])
                return super().form_valid(form)
        except DatabaseError as e:
            form.add_error(None, "An error occured")
            return self.form_invalid(form)
