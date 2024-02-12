from app_inquery.api.public.serializers.inquery import PublicAddInquerySerializer

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission


class PublicAddInqueryAPIView(generics.CustomCreateAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = PublicAddInquerySerializer
