from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField(db_comment="Yes/No")

    def __str__(self) -> str:
        return self.name
