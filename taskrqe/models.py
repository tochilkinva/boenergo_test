from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_zero(value):
    if value == 0:
        raise ValidationError(
            _('А не должно быть 0'),
            params={'value': value},
        )


class RQE(models.Model):
    coefa = models.FloatField(
        verbose_name='A',
        validators=[validate_zero, ]
    )
    coefb = models.FloatField(
        verbose_name='B'
    )
    coefc = models.FloatField(
        verbose_name='C'
    )

    root1 = models.FloatField(
        verbose_name='Корень 1',
        null=True,
        default=None,
    )
    root2 = models.FloatField(
        verbose_name='Корень 2',
        null=True,
        default=None,
    )

    class Meta:
        ordering = ('coefa',)
        verbose_name = 'Коэффициент квадратичного уравнения'
        verbose_name_plural = 'Коэффициенты квадратичного уравнения'

    def __str__(self):
        return (f'ABC: {self.coefa} {self.coefb} {self.coefc},'
                f'Root 12: {self.root1} {self.root2}')
