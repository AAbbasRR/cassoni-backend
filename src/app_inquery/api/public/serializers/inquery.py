from utils.serializers import serializer
from app_inquery.models import InQueryModel


class PublicAddInquerySerializer(serializer.CustomModelSerializer):
    class Meta:
        model = InQueryModel
        fields = ("mobile", "email")
