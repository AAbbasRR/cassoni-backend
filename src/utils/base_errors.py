from django.utils.translation import gettext_lazy as _


class BaseErrors:
    @classmethod
    def change_error_variable(cls, error_name, **kwargs):
        message = getattr(cls, error_name)
        for key, value in kwargs.items():
            message = message.replace("{%s}" % key, str(value))
        return message

    @classmethod
    def return_error_with_name(cls, error_name):
        return getattr(cls, error_name)

    # project
    url_not_found = _("URL Not Found.")
    server_error = _("Server Error.")

    # models
    video_format_error = _("Unsupported file extension. Please upload a video file.")

    # serializer
    object_not_found = _("{object} Not Found")
    parameter_is_required = _("parameter {param_name} is required")
