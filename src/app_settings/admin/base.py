from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AdminSiteSettingsAdmin(admin.AdminSite):
    site_title = _("Admin Panel")
    site_header = _("Admin Panel")
    index_title = _("Admin Panel")

    def each_context(self, request):
        context = super().each_context(request)
        # context.update({
        #     "order_count": Orders.objects.filter(status="AWC").exclude(
        #         submit_date__range=[timezone.now() - timezone.timedelta(hours=1), timezone.now()]).count()
        # })
        return context


admin_site = AdminSiteSettingsAdmin()
admin_site.register(UserModel)
