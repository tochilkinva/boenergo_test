from django.contrib import admin

from .models import Item


@admin.register(Item)
class RQEAdmin(admin.ModelAdmin):
    list_display = ("number", "color", "status")
    empty_value_display = "-пусто-"
