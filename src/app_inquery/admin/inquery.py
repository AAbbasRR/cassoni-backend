from django.contrib import admin

from app_settings.admin.base import admin_site
from app_inquery.models import InQueryModel


class InQueryAdmin(admin.ModelAdmin):
    list_display = ("mobile", "email", "create_at")
    readonly_fields = (
        "mobile",
        "email",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    class Meta:
        model = InQueryModel


admin_site.register(InQueryModel, InQueryAdmin)
