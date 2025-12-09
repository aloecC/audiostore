from django.contrib import admin
from library.models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    list_filter = ('birth_date',)  # Фильтрация
    search_fields = ('first_name', 'last_name',)  # Поиск


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')
    list_filter = ('title',)  # Фильтрация
    search_fields = ('title', 'author',)  # Поиск