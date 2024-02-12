from app_settings.api.public.serializers.video import PublicContainerVideoSerializer
from app_settings.models import ContainerVideoModel

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission
from utils.views.paginations import BasePagination


class PublicContainerVideoAPIView(generics.CustomListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicContainerVideoSerializer
    queryset = ContainerVideoModel.objects.all()
