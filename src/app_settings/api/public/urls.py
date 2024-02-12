from django.urls import path
from .views import *

app_name = "app_settings_public"
urlpatterns = [
    path(
        "contact/list/",
        PublicContactAPIView.as_view(),
        name="list_contact_public",
    ),
    path(
        "options/list/",
        PublicOptionsAPIView.as_view(),
        name="list_options_public",
    ),
    path(
        "social_media/list/",
        PublicSocialMediaAPIView.as_view(),
        name="list_social_media_public",
    ),
    path(
        "video/list/",
        PublicContainerVideoAPIView.as_view(),
        name="list_video_public",
    ),
]
