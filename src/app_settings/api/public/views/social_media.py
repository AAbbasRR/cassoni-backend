from app_settings.api.public.serializers.social_media import PublicSocialMediaSerializer
from app_settings.models import SocialMediaModel

from utils.views import generics
from utils.views.versioning import BaseVersioning
from utils.views.permissions import AllowAnyPermission
from utils.views.paginations import BasePagination


class PublicSocialMediaAPIView(generics.CustomListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = PublicSocialMediaSerializer
    queryset = SocialMediaModel.objects.all()
