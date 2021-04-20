from django.contrib import admin
from . import models


@admin.register(models.PortpolioModel)
class PortpolioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "url",
    )

    filter_horizontal = ("participants",)
