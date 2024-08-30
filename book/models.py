from django.db import models
import os
from category.models import Category


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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(db_comment="Yes/No")

    def __str__(self):
        return self.title
