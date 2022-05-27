from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)


    def __str__(self):
        return f'#{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('pk', )

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(verbose_name='Имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    short_desc = models.CharField(verbose_name='Краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='Цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'