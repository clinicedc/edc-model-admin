from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

model_admin_app_admin = EdcAdminSite(name="model_admin_app_admin", app_label=AppConfig.name)
