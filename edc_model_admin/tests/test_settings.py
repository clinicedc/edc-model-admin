#!/usr/bin/env python
import sys
from pathlib import Path

from edc_test_settings.default_test_settings import DefaultTestSettings

base_dir = Path(__file__).parent.parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    template_dirs=[str(base_dir / "tests" / "templates")],
    DEBUG=True,
    BASE_DIR=base_dir,
    APP_NAME="edc_model_admin",
    ETC_DIR=base_dir / "etc",
    DJANGO_CRYPTO_FIELDS_KEY_PATH=base_dir / "tests" / "etc",
    GIT_DIR=base_dir.parent,
    HOLIDAY_FILE=base_dir / "tests" / "holidays.csv",
    SILENCED_SYSTEM_CHECKS=[
        "sites.E101",
        "edc_sites.E001",
        "edc_navbar.E002",
        "edc_navbar.E003",
    ],
    ROOT_URLCONF="model_admin_app.urls",
    SUBJECT_SCREENING_MODEL="model_admin_app.subjectscreening",
    SUBJECT_CONSENT_MODEL="model_admin_app.subjectconsent",
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL="edc_visit_tracking.subjectvisitmissed",
    SUBJECT_REQUISITION_MODEL="model_admin_app.subjectrequisition",
    SUBJECT_APP_LABEL="model_admin_app",
    EDC_SITES_REGISTER_DEFAULT=True,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_extensions",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "multisite",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_form_runners.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_label.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_listboard.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "adverse_event_app",
        "model_admin_app.apps.AppConfig",
        "edc_appconfig.apps.AppConfig",
    ],
    DASHBOARD_BASE_TEMPLATES={
        "dashboard_template": str(base_dir / "tests" / "templates" / "dashboard.html"),
        "dashboard2_template": str(base_dir / "tests" / "templates" / "dashboard2.html"),
    },
    use_test_urls=False,
    add_dashboard_middleware=True,
).settings


for k, v in project_settings.items():
    setattr(sys.modules[__name__], k, v)
