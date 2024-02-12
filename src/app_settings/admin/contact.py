from django.contrib import admin

from app_settings.admin.base import admin_site
from app_settings.models import ContactModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ("type", "value")

    class Meta:
        model = ContactModel


admin_site.register(ContactModel, ContactAdmin)
