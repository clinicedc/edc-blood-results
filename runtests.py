#!/usr/bin/env python
import logging
from os.path import abspath, dirname, join

from edc_test_utils import DefaultTestSettings, func_main

base_dir = dirname(abspath(__file__))
app_name = "edc_lab_results"

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=join(base_dir, app_name, "tests", "etc"),
    SUBJECT_SCREENING_MODEL="edc_metadata.subjectscreening",
    SUBJECT_CONSENT_MODEL="edc_metadata.subjectconsent",
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL="edc_metadata.subjectvisitmissed",
    SUBJECT_REQUISITION_MODEL="edc_metadata.subjectrequisition",
    EDC_BLOOD_RESULTS_MODEL_APP_LABEL="edc_lab_results",
    LIST_MODEL_APP_LABEL="edc_metadata",
    EDC_SITES_REGISTER_DEFAULT=True,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "multisite",
        "edc_appointment.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_lab_results.apps.AppConfig",
    ],
    RANDOMIZATION_LIST_PATH=join(base_dir, app_name, "tests", "test_randomization_list.csv"),
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    func_main(project_settings, f"{app_name}.tests")


if __name__ == "__main__":
    logging.basicConfig()
    main()
