from django.views.generic import ListView
from .models import Book
from category.models import Category


class CategoryBookView(ListView):
    model = Book
    template_name = "core/home.html"
    context_object_name = "books"

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        return Book.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status=True).values(
            "id", "name", "slug"
        )
        return context
