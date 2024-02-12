from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.db.models import AbstractDateModel


class SocialMediaManager(models.Manager):
    pass


class SocialMedia(AbstractDateModel):
    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    class SocialApplications(models.TextChoices):
        Telegram = "Telegram", _("Telegram")
        WhatsApp = "WhatsApp", _("WhatsApp")
        YouTube = "YouTube", _("YouTube")
        Instagram = "Instagram", _("Instagram")
        Twitter = "Twitter", _("Twitter")

    application = models.CharField(
        max_length=10,
        choices=SocialApplications.choices,
        unique=True,
        verbose_name=_("Application"),
    )
    application_url = models.URLField(verbose_name=_("Application URL"))

    objects = SocialMediaManager()
