from django.views.generic import FormView, View
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction, DatabaseError
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages


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


class UserUpdateView(View):
    template_name = "profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect("profile")
        return render(request, self.template_name, {"form": form})
