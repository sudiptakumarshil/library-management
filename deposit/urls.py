from django.urls import path
from .views import DepositMoneyView

urlpatterns = [
    path("", DepositMoneyView.as_view(), name="deposit"),
]
