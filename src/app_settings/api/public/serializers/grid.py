from utils.serializers import serializer

from app_settings.models import ContainerGridImageModel


class PublicContainerImageSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = ContainerGridImageModel
        fields = ("image", "caption", "alt")
