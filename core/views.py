from django.shortcuts import render
from django.views.generic import TemplateView
from category.models import Category
from book.models import Book


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status=True).values(
            "id", "name", "slug"
        )
        context["books"] = Book.objects.filter(status=True)[:5]
        return context


