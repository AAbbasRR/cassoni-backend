from utils.serializers import serializer

from app_settings.models import ContainerGridImageModel


class PublicContainerImageSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = ContainerGridImageModel
        fields = ("image", "caption", "alt", "slug")


class PublicContainerImageDetailSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = ContainerGridImageModel
        fields = (
            "main_image",
            "main_image_alt",
            "main_video",
            "filter_bw",
            "main_image_content",
            "content",
        )
