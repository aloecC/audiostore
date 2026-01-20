from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (id, 'name', 'category', 'purchase_price')
    list_filter = ('category',)  # Фильтрация
    search_fields = ('name', 'description',)  # Поиск


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (id, 'name')
    list_filter = ('name',)  # Фильтрация
    search_fields = ('name', 'description',)  # Поиск

