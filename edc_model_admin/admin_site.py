from django.apps import apps as django_apps
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site

admin.site.enable_nav_sidebar = False


class EdcAdminSite(DjangoAdminSite):

    app_index_template = "edc_model_admin/admin/app_index.html"
    enable_nav_sidebar = False  # DJ 3.1
    final_catch_all_view = False  # DJ 3.2
    site_url = "/administration/"

    def __init__(self, name="admin", app_label=None):
        self.app_label = app_label
        super().__init__(name)
        del self._actions["delete_selected"]

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        context.update(
            site_title=self.get_edc_site_title(request),
            site_header=self.get_edc_site_header(request),
            index_title=self.index_title,
        )
        return context

    def get_edc_site_title(self, request):
        verbose_name = django_apps.get_app_config(self.app_label).verbose_name
        return verbose_name.replace(
            settings.EDC_PROTOCOL_PROJECT_NAME,
            (
                f"{settings.EDC_PROTOCOL_PROJECT_NAME} @ "
                f"{get_current_site(request).name.title()}: "
            ),
        )

    def get_edc_site_header(self, request):
        return self.get_edc_site_title(request)

    """
    To inlcude this in the administration section set
    `AppConfig.include_in_administration_section = True`
    in your apps.py. (See also View `edc_dashboard.administration.py`).

    Add to your project urls.py
        path("admin/", edc_action_item.urls),

    if set to include_in_administration_section=True, add a local `urls.py`

        from django.urls import path
        from django.views.generic.base import RedirectView

        from .admin_site import edc_action_item_admin

        app_name = "edc_action_item"

        urlpatterns = [
            path("admin/", edc_action_item.urls),
            path("", RedirectView.as_view(url=f"/{app_name}/admin/"), name="home_url"),
        ]

    and then add to your project urls.py

        path("edc_action_item/", include("edc_action_item.urls")),

    """
