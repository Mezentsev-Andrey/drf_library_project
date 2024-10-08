# Generated by Django 4.2.9 on 2024-08-17 18:11

import django.db.models.deletion
import simple_history.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название книги"),
                ),
                ("author", models.CharField(max_length=100, verbose_name="Автор")),
                (
                    "genre",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Жанр"
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="books/",
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Аннотация"),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="BorrowedBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "borrowed_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата получения книги"
                    ),
                ),
                (
                    "returned_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата возврата книги"
                    ),
                ),
                ("returned", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Взятая книга",
                "verbose_name_plural": "Взятые книги",
            },
        ),
        migrations.CreateModel(
            name="HistoricalBook",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название книги"),
                ),
                ("author", models.CharField(max_length=100, verbose_name="Автор")),
                (
                    "genre",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Жанр"
                    ),
                ),
                (
                    "cover",
                    models.TextField(
                        blank=True, max_length=100, null=True, verbose_name="Обложка"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Аннотация"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Книга",
                "verbose_name_plural": "historical Книги",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalBorrowedBook",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "borrowed_date",
                    models.DateTimeField(
                        blank=True, editable=False, verbose_name="Дата получения книги"
                    ),
                ),
                (
                    "returned_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата возврата книги"
                    ),
                ),
                ("returned", models.BooleanField(default=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="library.book",
                        verbose_name="Взятая книга",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Взятая книга",
                "verbose_name_plural": "historical Взятые книги",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
