from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from utils.db.models import AbstractDateModel


class OptionsManager(models.Manager):
    pass


class Options(AbstractDateModel):
    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    class TypeOptions(models.TextChoices):
        OurStory = "OurStory", _("OurStory")

    type = models.CharField(
        max_length=10, choices=TypeOptions.choices, unique=True, verbose_name=_("Type")
    )
    value = RichTextUploadingField(verbose_name=_("Value"))
