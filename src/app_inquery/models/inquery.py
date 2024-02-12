from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.db.models import AbstractDateModel


class InQueryManager(models.Manager):
    pass


class InQuery(AbstractDateModel):
    class Meta:
        verbose_name = _("InQuery")
        verbose_name_plural = _("InQueries")

    mobile = models.CharField(
        max_length=15, null=True, blank=True, verbose_name=_("Mobile")
    )
    email = models.EmailField(null=True, blank=True, verbose_name=_("Email"))

    objects = InQueryManager()
