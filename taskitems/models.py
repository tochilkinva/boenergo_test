from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_zero(value):
    if value == 0:
        raise ValidationError(
            _('Номер коробки не должен быть 0'),
            params={'value': value},
        )


class Item(models.Model):
    class Colors(models.TextChoices):
        RED = 'RED', 'Красный'
        GREEN = 'GREEN', 'Зеленый'
        BLUE = 'BLUE', 'Синий'

    color = models.CharField(
        max_length=256,
        choices=Colors.choices,
        default=Colors.RED,
        verbose_name='Цвет предмета',
    )

    number = models.PositiveIntegerField(
        verbose_name='Номер предмета',
        validators=[
            validate_zero,
            MinValueValidator(1),
            MaxValueValidator(100),
        ],
    )

    status = models.BooleanField(
        verbose_name='Цвет разгадан',
        default=False,
    )

    class Meta:
        ordering = ('number',)
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'№ {self.number} - {self.color} - {self.status}'
