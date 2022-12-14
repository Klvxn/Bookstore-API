# Generated by Django 4.1 on 2022-08-31 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0016_rename_description_book_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="about",
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="author",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books_published",
                to="books.publisher",
            ),
        ),
        migrations.AlterField(
            model_name="publisher",
            name="address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="publisher",
            name="slug",
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name="publisher",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True, related_name="subscribed_to", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
