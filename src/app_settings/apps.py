from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_settings"
    verbose_name = _("App Setting")
    verbose_name_plural = _("App Settings")

    def ready(self):
        import app_settings.signals.video
