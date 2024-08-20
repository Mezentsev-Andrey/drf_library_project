from datetime import timedelta

from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Book(models.Model):
    """
    Модель, представляющая книгу в библиотеке.
    """

    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    genre = models.CharField(max_length=50, verbose_name="Жанр", **NULLABLE)
    cover = models.ImageField(upload_to="books/", verbose_name="Обложка", **NULLABLE)
    description = models.TextField(verbose_name="Аннотация", **NULLABLE)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BorrowedBook(models.Model):
    """
    Модель, представляющая взятую книгу пользователем.
    """

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, verbose_name="Взятая книга"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Читатель")
    borrowed_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата получения книги"
    )
    returned_date = models.DateTimeField(verbose_name="Дата возврата книги", **NULLABLE)
    is_returned = models.BooleanField(default=False, verbose_name="Книга возвращена")
    history = HistoricalRecords()

    def days_borrowed(self):
        if self.returned_date:
            end_date = self.returned_date
        else:
            end_date = timezone.now()

        borrowed_date = (
            timezone.make_aware(self.borrowed_date)
            if timezone.is_naive(self.borrowed_date)
            else self.borrowed_date
        )
        return (end_date - borrowed_date).days

    @property
    def return_date(self):
        return self.borrowed_date + timedelta(days=14) if self.is_returned else None

    class Meta:
        verbose_name = "Взятая книга"
        verbose_name_plural = "Взятые книги"
