# Generated by Django 3.2.7 on 2021-09-23 08:03

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discount', '0003_auto_20210923_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='deliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 11, 3, 12, 571319), verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 11, 3, 12, 571319), verbose_name='Время заказа'),
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user_id',
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
