# Generated by Django 4.2.9 on 2024-08-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_rename_returned_borrowedbook_is_returned_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowedbook",
            name="is_returned",
            field=models.BooleanField(default=False, verbose_name="Книга возвращена"),
        ),
        migrations.AlterField(
            model_name="historicalborrowedbook",
            name="is_returned",
            field=models.BooleanField(default=False, verbose_name="Книга возвращена"),
        ),
    ]
