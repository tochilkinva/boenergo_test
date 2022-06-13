from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['number', 'color', ]
        labels = {
            'number': _('Номер предмета'),
            'color': _('Цвет предмета'),
        }
        help_texts = {
            'number': _('Укажите номер предмета'),
            'color': _('Укажите цвет предмета'),
        }
