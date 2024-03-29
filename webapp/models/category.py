from django.db import models


class Category(models.Model):
    category = models.CharField(
        max_length=50,
        verbose_name='Категория'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время изменения'
    )

    def __str__(self):
        return self.category
