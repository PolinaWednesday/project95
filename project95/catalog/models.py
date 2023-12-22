from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    product_title = models.TextField(max_length=500, verbose_name="Описание продукта")
    product_image = models.ImageField(upload_to="products/", verbose_name="Изображение продукта", **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория продукта")
    product_price = models.IntegerField(verbose_name="Цена продукта")
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    product_create_added = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')

    def __str__(self):
        return f'{self.product_name} - {self.product_title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Наименование категории")
    category_title = models.TextField(max_length=500, verbose_name="Описание категории")

    def __str__(self):
        return f'{self.category_name} - {self.category_title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
