from django.urls import path
from .views import CategoryBookView

urlpatterns = [
    path("category-book/<slug:slug>/", CategoryBookView.as_view(), name="book.category_book")
]
