from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction, DatabaseError


class UserRegistrationView(FormView):
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = form.save()
                login(self.request, user)
                return super().form_valid(form)
        except DatabaseError as e:
            form.add_error(None, "An error occured")
            return self.form_invalid(form)


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy("home")
