from django import forms
from django.utils.translation import gettext_lazy as _

from .models import RQE


class RQEForm(forms.ModelForm):
    class Meta:
        model = RQE
        fields = ['coefa', 'coefb', 'coefc']
        labels = {
            'coefa': _('Коэффициент A'),
            'coefb': _('Коэффициент B'),
            'coefc': _('Коэффициент C'),
        }
        help_texts = {
            'coefa': _('Добавьте значение коэффициента A'),
            'coefb': _('Добавьте значение коэффициента B'),
            'coefc': _('Добавьте значение коэффициента C'),
        }
