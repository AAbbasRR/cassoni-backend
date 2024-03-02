from django.contrib import admin
from django.utils.html import format_html

from app_settings.admin.base import admin_site
from app_settings.models import ContainerGridImageModel


class ContainerImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "image_preview", "alt")

    def image_preview(self, obj):
        image_file = obj.image

        return format_html(
            '<img src="{}" width="50px" height="50px" />',
            image_file.url,
        )

    image_preview.short_description = "Image Preview"

    class Meta:
        model = ContainerGridImageModel


admin_site.register(ContainerGridImageModel, ContainerImageAdmin)
