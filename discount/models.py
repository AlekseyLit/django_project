import datetime

from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.TextField('Описание')

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
        return self.product + " " + self.brand + " " + self.model + " " + f"{self.price}" + " " + f"{self.discount}"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Offers(models.Model):
    company = models.CharField('Компания', max_length=150)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    offer = models.TextField('Предложение')

    def __str__(self):
        return self.company + "  " + self.offer

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class Orders(models.Model):
    user_id = models.ManyToManyField(User)
    price = models.DecimalField('Сумма заказа', decimal_places=0, max_digits=20)
    orderDate = models.DateTimeField('Время заказа', default=datetime.datetime.now())
    deliveryDate = models.DateTimeField('Время доставки', default=datetime.datetime.now())

    def __str__(self):
        return f"{self.price}" + "   " + f"{self.orderDate}" + "  " +f"{self.deliveryDate}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'