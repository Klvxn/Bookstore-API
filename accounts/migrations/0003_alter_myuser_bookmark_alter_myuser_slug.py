# Generated by Django 4.1 on 2022-08-31 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0017_alter_author_about_alter_author_slug_and_more"),
        ("accounts", "0002_myuser_bookmark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="bookmark",
            field=models.ManyToManyField(
                blank=True, related_name="bookmark", to="books.book"
            ),
        ),
        migrations.AlterField(
            model_name="myuser",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
