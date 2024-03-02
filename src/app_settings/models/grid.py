from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.db.models import AbstractDateModel


class ContainerImageManager(models.Manager):
    pass


def image_directory_path(instance, filename):
    return "image/{0}".format(filename)


class ContainerGridImage(AbstractDateModel):
    class Meta:
        verbose_name = _("Container Grid Image")
        verbose_name_plural = _("Container Grid Image")

    image = models.ImageField(
        upload_to=image_directory_path,
        verbose_name=_("Image File"),
    )
    caption = models.CharField(
        max_length=128,
        verbose_name=_("Caption")
    )
    alt = models.CharField(
        max_length=128,
        verbose_name=_("Alt")
    )


    objects = ContainerImageManager()
