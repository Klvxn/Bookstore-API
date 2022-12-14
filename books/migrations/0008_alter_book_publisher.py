# Generated by Django 4.1 on 2022-08-25 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_alter_author_about_alter_book_publisher_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books_published",
                to="books.publisher",
            ),
        ),
    ]
