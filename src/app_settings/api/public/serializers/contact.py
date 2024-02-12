from utils.serializers import serializer

from app_settings.models import ContactModel


class PublicContactSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = ContactModel
        fields = ("type", "value")
