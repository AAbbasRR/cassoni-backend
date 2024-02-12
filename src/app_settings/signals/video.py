from django.db.models.signals import pre_delete
from django.dispatch import receiver

from app_settings.models import ContainerVideoModel

import os


@receiver(pre_delete, sender=ContainerVideoModel)
def delete_video_file_on_delete(sender, instance, **kwargs):
    if instance.video:
        video_path = instance.video.path
        if os.path.exists(video_path):
            os.remove(video_path)
