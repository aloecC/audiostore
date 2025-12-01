from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views_count')
    list_filter = ('created_at',)  # Фильтрация
    search_fields = ('title', 'tresh',)  # Поиск

