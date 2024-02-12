from django.contrib import admin

from app_settings.admin.base import admin_site
from app_settings.models import OptionsModel


class OptionsAdmin(admin.ModelAdmin):
    list_display = ("type", "brief_value")

    def brief_value(self, obj):
        return obj.value[:100] + "..." if len(obj.value) > 100 else obj.value

    class Meta:
        model = OptionsModel


admin_site.register(OptionsModel, OptionsAdmin)
