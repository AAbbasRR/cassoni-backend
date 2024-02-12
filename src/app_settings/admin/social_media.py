from django.contrib import admin

from app_settings.admin.base import admin_site
from app_settings.models import SocialMediaModel


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("application", "application_url")

    class Meta:
        model = SocialMediaModel


admin_site.register(SocialMediaModel, SocialMediaAdmin)
