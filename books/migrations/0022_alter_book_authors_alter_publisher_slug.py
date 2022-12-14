# Generated by Django 4.0 on 2022-10-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_alter_book_authors_alter_book_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books_written', to='books.Author'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
