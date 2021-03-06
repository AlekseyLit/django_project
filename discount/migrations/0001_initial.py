# Generated by Django 3.2.7 on 2021-09-21 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=150, verbose_name='Продукт')),
                ('brand', models.CharField(max_length=150, verbose_name='Брэнд')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('price', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='Цена')),
                ('discount', models.FloatField(verbose_name='Скидка')),
                ('company', models.CharField(max_length=150, verbose_name='Компания')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.categories')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]
