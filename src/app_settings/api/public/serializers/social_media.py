from utils.serializers import serializer

from app_settings.models import SocialMediaModel


class PublicSocialMediaSerializer(serializer.CustomModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = ("application", "application_url")
