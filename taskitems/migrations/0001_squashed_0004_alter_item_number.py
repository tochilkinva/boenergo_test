# Generated by Django 3.2.13 on 2022-06-13 16:39

import django.core.validators
from django.db import migrations, models

import taskitems.models


class Migration(migrations.Migration):

    replaces = [('taskitems', '0001_initial'), ('taskitems', '0002_alter_item_color'), ('taskitems', '0003_auto_20220613_1540'), ('taskitems', '0004_alter_item_number')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('RED', 'Красный'), ('GREEN', 'Зеленый'), ('BLUE', 'Синий')], default='RED', max_length=256, verbose_name='Цвет предмета')),
                ('number', models.PositiveIntegerField(validators=[taskitems.models.validate_zero, django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Номер предмета')),
                ('status', models.BooleanField(default=False, verbose_name='Цвет разгадан')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ('number',),
            },
        ),
    ]
