from app_settings.api.public.serializers.grid import PublicContainerImageSerializer
from app_settings.models import ContainerGridImageModel

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission
from utils.views.paginations import BasePagination


class PublicContainerImageAPIView(generics.CustomListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicContainerImageSerializer
    queryset = ContainerGridImageModel.objects.all()
