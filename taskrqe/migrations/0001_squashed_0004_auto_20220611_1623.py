# Generated by Django 3.2.13 on 2022-06-13 16:38

from django.db import migrations, models

import taskrqe.models


class Migration(migrations.Migration):

    replaces = [('taskrqe', '0001_initial'), ('taskrqe', '0002_auto_20220611_1612'), ('taskrqe', '0003_auto_20220611_1615'), ('taskrqe', '0004_auto_20220611_1623')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RQE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coefa', models.FloatField(validators=[taskrqe.models.validate_zero], verbose_name='A')),
                ('coefb', models.FloatField(verbose_name='B')),
                ('coefc', models.FloatField(verbose_name='C')),
                ('root1', models.FloatField(default=None, null=True, verbose_name='Корень 1')),
                ('root2', models.FloatField(default=None, null=True, verbose_name='Корень 2')),
            ],
            options={
                'verbose_name': 'Коэффициент квадратичного уравнения',
                'verbose_name_plural': 'Коэффициенты квадратичного уравнения',
                'ordering': ('coefa',),
            },
        ),
    ]