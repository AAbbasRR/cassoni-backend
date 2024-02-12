from app_settings.api.public.serializers.options import PublicOptionsSerializer
from app_settings.models import OptionsModel

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission
from utils.views.paginations import BasePagination


class PublicOptionsAPIView(generics.CustomListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicOptionsSerializer
    search_fields = ["type"]
    queryset = OptionsModel.objects.all()
