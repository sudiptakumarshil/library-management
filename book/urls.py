from django.urls import path
from .views import CategoryBookView, BookDetailView

urlpatterns = [
    path("category-book/<slug:slug>/", CategoryBookView.as_view(), name="book.category_book"),
    path("detail/<int:pk>/", BookDetailView.as_view(), name="book.detail"),
]
