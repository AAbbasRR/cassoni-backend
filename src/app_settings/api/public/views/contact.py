from app_settings.api.public.serializers.contact import PublicContactSerializer
from app_settings.models import ContactModel

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission
from utils.views.paginations import BasePagination


class PublicContactAPIView(generics.CustomListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicContactSerializer
    queryset = ContactModel.objects.all()
