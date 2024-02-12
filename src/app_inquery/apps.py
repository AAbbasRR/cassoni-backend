from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppInqueryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_inquery"
    verbose_name = _("App InQuery")
    verbose_name_plural = _("App InQueries")
