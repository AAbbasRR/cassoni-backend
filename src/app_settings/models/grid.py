from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from utils.db.models import AbstractDateModel
from utils.db.validators import validate_video_file_extension


class ContainerImageManager(models.Manager):
    pass


def image_directory_path(instance, filename):
    return "image/{0}".format(filename)


def video_directory_path(instance, filename):
    return "image/{0}".format(filename)


class ContainerGridImage(AbstractDateModel):
    class Meta:
        verbose_name = _("Container Grid Image")
        verbose_name_plural = _("Container Grid Image")

    image = models.ImageField(
        upload_to=image_directory_path,
        verbose_name=_("Image File Cover"),
    )
    caption = models.CharField(
        max_length=128,
        verbose_name=_("Caption")
    )
    alt = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_("Alt")
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_("Slug Link Page")
    )
    main_video = models.FileField(
        upload_to=video_directory_path,
        validators=[validate_video_file_extension],
        verbose_name=_("Video File"),
    )
    filter_bw = models.BooleanField(
        default=False, verbose_name=_("Video Have Filter Black & White?")
    )
    main_image = models.ImageField(
        upload_to=image_directory_path,
        verbose_name=_("Main Image File"),
    )
    main_image_alt = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_("Main Image Alt")
    )
    main_image_content = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name=_("Main Image Content"),
    )
    content = RichTextUploadingField(verbose_name=_("Content"))

    objects = ContainerImageManager()
