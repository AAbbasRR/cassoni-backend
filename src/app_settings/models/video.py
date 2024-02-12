from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.db.models import AbstractDateModel
from utils.db.validators import validate_video_file_extension


class ContainerVideoManager(models.Manager):
    pass


def video_directory_path(instance, filename):
    return "video/{0}".format(filename)


class ContainerVideo(AbstractDateModel):
    class Meta:
        verbose_name = _("Container Video")
        verbose_name_plural = _("Container Video")

    video = models.FileField(
        upload_to=video_directory_path,
        validators=[validate_video_file_extension],
        verbose_name=_("Video File"),
    )
    filter_bw = models.BooleanField(
        default=False, verbose_name=_("Have Filter Black & White?")
    )

    objects = ContainerVideoManager()
