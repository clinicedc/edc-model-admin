#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname


app_name = 'edc_model_admin'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    template_dirs=[os.path.join(
        base_dir, "edc_model_admin", "tests", "templates")],
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_extensions',
        'django_crypto_fields.apps.AppConfig',
        'django_revision.apps.AppConfig',
        'edc_base.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_dashboard.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_metadata_rules.apps.AppConfig',
        'edc_protocol.apps.AppConfig',
        'edc_reference.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'edc_timepoint.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'edc_model_admin.apps.EdcAppointmentAppConfig',
        'edc_model_admin.apps.EdcFacilityAppConfig',
        'edc_model_admin.apps.EdcMetadataAppConfig',
        'edc_model_admin.apps.EdcVisitTrackingAppConfig',
        'edc_model_admin.apps.AppConfig',
    ],
    DASHBOARD_URL_NAMES={
        'subject_dashboard_url': 'dashboard_app:subject_dashboard_url',
    },
    DASHBOARD_BASE_TEMPLATES={
        'subject_dashboard_template': os.path.join(
            base_dir, 'edc_model_admin', "tests", 'templates', "dashboard.html")},
    use_test_urls=True,
    add_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(
        failfast=True, tags=tags).run_tests([f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
