from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.db.models import AbstractDateModel


class ContactManager(models.Manager):
    pass


class Contact(AbstractDateModel):
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")
        ordering = ("type",)

    class TypeOptions(models.TextChoices):
        Phone = "Phone", _("Phone")
        Email = "Email", _("Email")
        Address = "Address", _("Address")

    type = models.CharField(
        max_length=8, choices=TypeOptions.choices, verbose_name=_("Type")
    )
    value = models.CharField(max_length=100, verbose_name=_("Value"))

    objects = ContactManager()
