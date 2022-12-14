from django.contrib import admin

from .models import Author, Book, Publisher


# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):

    list_display = ["name", "email", "website"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ["first_name", "last_name", "email"]
    ordering = ["first_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ["title", "publisher", "page_count"]
    list_filter = ["publisher", "authors"]
    search_fields = ["authors", "publisher"]
