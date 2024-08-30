from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from category.models import Category


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(status=True).values(
            "id", "name"
        )
        return context


class BookDetailView(View):
    template_name = "details.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
