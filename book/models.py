from django.db import models
import os
from category.models import Category
from user.models import User


def upload_to(instance, filename):
    app_label = instance._meta.app_label
    return os.path.join(app_label, "uploads", filename)


class Book(models.Model):
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to=upload_to)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.BooleanField(db_comment="Yes/No")

    def __str__(self):
        return self.title


class BorrowBook(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    book = models.OneToOneField(Book, related_name="book", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    return_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return self.book.title
