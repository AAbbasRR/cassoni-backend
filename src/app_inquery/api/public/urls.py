from django.urls import path
from .views import *

app_name = "app_inquery_public"
urlpatterns = [
    path(
        "new/submit/",
        PublicAddInqueryAPIView.as_view(),
        name="new_inquery_public",
    ),
]
