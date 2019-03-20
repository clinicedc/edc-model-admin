#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from os.path import abspath, dirname, join


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


base_dir = dirname(abspath(__file__))
app_name = 'edc_model_admin'

installed_apps = [
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
]

DEFAULT_SETTINGS = dict(
    BASE_DIR=base_dir,
    SITE_ID=40,
    ALLOWED_HOSTS=['localhost'],
    # AUTH_USER_MODEL='custom_user.CustomUser',
    ROOT_URLCONF=f'{app_name}.tests.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(base_dir, 'db.sqlite3'),
        }
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [join(base_dir, "edc_model_admin", "tests", "templates")],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'edc_dashboard.middleware.DashboardMiddleware',
        'edc_subject_dashboard.middleware.DashboardMiddleware',
    ],

    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,

    APP_NAME=app_name,
    COUNTRY='botswana',
    EDC_BOOTSTRAP=None,
    ETC_DIR=join(base_dir, 'etc'),

    DASHBOARD_URL_NAMES={
        'subject_dashboard_url': 'dashboard_app:subject_dashboard_url',
    },
    DASHBOARD_BASE_TEMPLATES={
        'subject_dashboard_template': os.path.join(base_dir, 'edc_model_admin', "tests", 'templates', "dashboard.html")},
    # DEBUG=False,
    # KEY_PATH=os.path.join(base_dir, 'etc'),
    # AUTO_CREATE_KEYS=True,

    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    MIGRATION_MODULES=DisableMigrations(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),
)

# update settings if running runtests directly from the command line
if __file__ == sys.argv[0]:
    key_path = os.path.join(base_dir, 'etc')
    DEFAULT_SETTINGS.update(
        DEBUG=False,
        KEY_PATH=key_path,
        AUTO_CREATE_KEYS=False)
    if len(os.listdir(key_path)) == 0:
        DEFAULT_SETTINGS.update(AUTO_CREATE_KEYS=True)

if os.environ.get("TRAVIS"):
    DEFAULT_SETTINGS.update(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'edc',
                'USER': 'travis',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
            },
        })


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
