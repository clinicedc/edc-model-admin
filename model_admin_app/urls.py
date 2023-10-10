from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from edc_utils.paths_for_urlpatterns import paths_for_urlpatterns

from .admin_site import model_admin_app_admin
from .views import CrfOneListView, HomeView

app_name = "model_admin_app"


urlpatterns = []

for app_name in [
    "edc_dashboard",
    "edc_auth",
    "edc_export",
    "edc_consent",
    "edc_device",
    "edc_protocol",
    "edc_reference",
    "edc_visit_schedule",
    # "model_admin_app",
]:
    for p in paths_for_urlpatterns(app_name):
        urlpatterns.append(p)

urlpatterns += [
    path("admin/", model_admin_app_admin.urls),
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", include("edc_model_admin.tests.dashboard_app.urls")),
    path("", include("edc_model_admin.tests.dashboard2_app.urls")),
    path("", CrfOneListView.as_view(), name="crfone-list"),
    path("", HomeView.as_view(), name="home_url"),
    path("", HomeView.as_view(), name="administration_url"),
    path("", RedirectView.as_view(url="admin/"), name="logout"),
]
