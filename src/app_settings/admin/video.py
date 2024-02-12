from django.contrib import admin
from django.utils.html import format_html

from app_settings.admin.base import admin_site
from app_settings.models import ContainerVideoModel


class ContainerVideoAdmin(admin.ModelAdmin):
    list_display = ("video_preview", "filter_bw")

    def video_preview(self, obj):
        # Change 'video_field' to the name of your video field
        video_file = obj.video

        # Return HTML code for embedding video preview
        return format_html(
            '<video width="240" height="120" controls>'
            '<source src="{}" type="video/mp4">'
            "Your browser does not support the video tag."
            "</video>",
            video_file.url,
        )

    video_preview.short_description = "Video Preview"

    def has_add_permission(self, request):
        if ContainerVideoModel.objects.count() >= 1:
            return False
        return True

    class Meta:
        model = ContainerVideoModel


admin_site.register(ContainerVideoModel, ContainerVideoAdmin)
