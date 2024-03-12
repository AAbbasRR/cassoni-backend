from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app_settings.admin import base_admin
from django.conf.urls.i18n import i18n_patterns

v1_public_urlpatterns = [
    path(
        "settings/",
        include("app_settings.api.public.urls", namespace="app_settings_public"),
    ),
    path(
        "inquery/",
        include("app_inquery.api.public.urls", namespace="app_inquery_public"),
    ),
]

v1_urlpatterns = [
    path("public/", include(v1_public_urlpatterns)),
]

urlpatterns = [
    path("admin/", base_admin.admin_site.urls),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path("api/<str:version>/", include(v1_urlpatterns)),
]

urlpatterns += i18n_patterns(
    *urlpatterns,
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

handler404 = "utils.url_handlers.custom_404_response"
handler500 = "utils.url_handlers.custom_500_response"
