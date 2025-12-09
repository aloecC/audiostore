from django import forms
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

    def clean_purchase_price(self):  # Исправлено имя метода на clean_purchase_price
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price is not None and purchase_price < 0:  # Проверяем на None
            raise ValidationError('Цена не может быть отрицательной.')
        return purchase_price  # Возвращаем очищенное значение