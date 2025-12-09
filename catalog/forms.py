import os

from django import forms
from django.core.files.images import get_image_dimensions

from .models import Product, Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if name in forbidden_words:
            self.add_error('name', 'Поле "название" содержит запрещенное слово')

            # Разделяем описание на слова
        words_in_description = description.split()

        for word in words_in_description:
            # Приводим слово к нижнему регистру для проверки
            normalized_word = word.lower().strip(",.!?;:()[]{}")  # Убираем знаки препинания
            if normalized_word in forbidden_words:
                self.add_error('description', 'Поле "описание" содержит запрещенное слово')
                break  # Можно выйти из цикла после первой найденной ошибки


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Добавьте изображение'
            }
        )

        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            }
        )

        self.fields['purchase_price'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if name in forbidden_words:
            self.add_error('name', 'Поле "название" содержит запрещенное слово')

            # Разделяем описание на слова
        words_in_description = description.split()

        for word in words_in_description:
            # Приводим слово к нижнему регистру для проверки
            normalized_word = word.lower().strip(",.!?;:()[]{}")  # Убираем знаки препинания
            if normalized_word in forbidden_words:
                self.add_error('description', 'Поле "описание" содержит запрещенное слово')
                break  # Можно выйти из цикла после первой найденной ошибки

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price is not None and purchase_price < 0:  # Проверяем на None
            raise ValidationError('Цена не может быть отрицательной.')
        return purchase_price  # Возвращаем очищенное значение

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверяем формат файла
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError('Допустимые форматы: JPEG и PNG.')

            # Проверяем размер файла (5 МБ)
            if image.size > 5 * 1024 * 1024:  # 5 МБ в байтах
                raise ValidationError('Размер файла не должен превышать 5 МБ.')

            # Дополнительная проверка размеров изображения
            width, height = get_image_dimensions(image)
            if width > 2000 or height > 2000:  # Пример ограничения на размеры
                raise ValidationError('Ширина и высота изображения не должны превышать 2000 пикселей.')

        return image