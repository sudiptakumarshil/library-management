from django.views.generic import ListView
from .models import Book
from category.models import Category
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from book.models import BorrowBook


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
            return self.handle_borrow_now(request, book)
        return self.get(request, *args, **kwargs)

    def handle_borrow_now(self, request, book):
        borrowDictionary = {
            "user": request.user,
            "book": book,
            "price": book.price,
        }

        transaction = BorrowBook.objects.create(**borrowDictionary)
        transaction.save()

        messages.success(request, "Thank you for your purchase!")
        return redirect("home")
