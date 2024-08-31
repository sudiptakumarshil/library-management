from django.views.generic import ListView
from .models import Book
from category.models import Category
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from book.models import BorrowBook
from django.db import transaction, DatabaseError
from user.models import UserAccount


class CategoryBookView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        return Book.objects.filter(category__slug=category_slug, status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status=True).values(
            "id", "name", "slug"
        )
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "details.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status=True).values(
            "id", "name", "slug"
        )
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        if "borrow_now" in request.POST:
            return self.handle_borrow_now(request, book, *args, **kwargs)
        return self.get(request, *args, **kwargs)

    def handle_borrow_now(self, request, book, *args, **kwargs):
        borrowDictionary = {
            "user": request.user,
            "book": book,
            "price": book.price,
        }

        try:
            with transaction.atomic():
                account = get_object_or_404(UserAccount, user=request.user)

                if account.balance > book.price:
                    account.balance -= book.price
                    account.save()

                    borrow = BorrowBook.objects.create(**borrowDictionary)
                    borrow.save()

                    messages.success(request, "Thank you for your purchase!")
                    return redirect('home')

                messages.error(request, "Sorry! You do not have sufficient balance.")
                return self.get(request, *args, **kwargs)

        except DatabaseError as e:
            messages.error(request, "Sorry! a database error occured.")
            return self.get(request, *args, **kwargs)
