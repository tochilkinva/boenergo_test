from django.contrib import admin

from .models import RQE


@admin.register(RQE)
class RQEAdmin(admin.ModelAdmin):
    list_display = ("coefa", "coefb", "coefc", 'root1', 'root2')
    empty_value_display = "-пусто-"
