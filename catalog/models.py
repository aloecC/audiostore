from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']  #Порядок сортировки


class Product(models.Model):
    name = models.CharField(help_text='Введите имя', max_length=100, verbose_name='Имя')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография', upload_to='photos/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='категории')
    purchase_price = models.IntegerField(help_text='Введите цену', verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.purchase_price} {self.updated_at}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['purchase_price']  #Порядок сортировки




