from utils.serializers import serializer

from app_settings.models import OptionsModel


class PublicOptionsSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = OptionsModel
        fields = ("type", "value")
