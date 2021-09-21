from django.db import models


class Categories(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Discounts(models.Model):
    product = models.CharField('Продукт', max_length=150)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.CharField('Брэнд', max_length=150)
    model = models.CharField('Модель', max_length=150)
    price = models.DecimalField('Цена', decimal_places=0, max_digits=20)
    discount = models.FloatField('Скидка')
    company = models.CharField('Компания', max_length=150)

    def __str__(self):
        return self.product + " " + self.model + " " + f"{self.price}" + " " + f"{self.discount}"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'