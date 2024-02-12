from django.core.validators import ValidationError

from utils import BaseErrors

import os


def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".mp4", ".avi", ".mov", ".wmv"]
    if not ext.lower() in valid_extensions:
        raise ValidationError(BaseErrors.video_format_error)
