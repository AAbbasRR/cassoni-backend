from utils.serializers import serializer

from app_settings.models import ContainerVideoModel


class PublicContainerVideoSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = ContainerVideoModel
        fields = ("video", "filter_bw")
