# Generated by Django 4.0 on 2022-10-02 17:41

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('books', '0022_alter_book_authors_alter_publisher_slug'),
        ('accounts', '0003_alter_myuser_bookmark_alter_myuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to='books.Book'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='get_full_name', unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
