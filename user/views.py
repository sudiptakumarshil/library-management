from django.views.generic import FormView, TemplateView, View
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction, DatabaseError
from django.shortcuts import redirect
from django.contrib import messages
from book.models import BorrowBook
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect


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


class UserUpdateView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserUpdateForm(instance=self.request.user)
        context["borrowed_books"] = BorrowBook.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect("profile")
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class ReturnBookView(View):
    def get(self, request, id):
        try:
            with transaction.atomic():
                obj = get_object_or_404(BorrowBook, id=id)

                obj.return_date = timezone.now()
                obj.save()

                obj.user.account.balance += obj.price
                obj.user.account.save()

        except DatabaseError as e:
            print(f"An error occurred: {e}")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
