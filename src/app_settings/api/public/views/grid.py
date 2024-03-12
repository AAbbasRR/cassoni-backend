from app_settings.api.public.serializers.grid import (
    PublicContainerImageSerializer,
    PublicContainerImageDetailSerializer
)
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


class PublicContainerImageDetailAPIView(generics.CustomRetrieveAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicContainerImageDetailSerializer
    queryset = ContainerGridImageModel.objects.all()
    lookup_in_parameter = False
    lookup_field = "slug"
