import uuid
from datetime import date

from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_lab.model_mixins import RequisitionModelMixin
from edc_model.models import BaseUuidModel
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_screening.model_mixins import ScreeningModelMixin
from edc_sites.models import SiteModelMixin
from edc_utils import get_utcnow
from edc_visit_schedule.model_mixins import OffScheduleModelMixin, OnScheduleModelMixin


class SubjectScreening(ScreeningModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()


class BasicModel(SiteModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)
    f3 = models.CharField(max_length=10, null=True, blank=False)
    f4 = models.CharField(max_length=10, null=True, blank=False)
    f5 = models.CharField(max_length=10)
    f5_other = models.CharField(max_length=10, null=True)
    subject_identifier = models.CharField(max_length=25, default="12345")


class OnSchedule(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffSchedule(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class SubjectConsent(
    SiteModelMixin,
    NonUniqueSubjectIdentifierFieldMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    BaseUuidModel,
):
    report_datetime = models.DateTimeField(default=get_utcnow)

    consent_datetime = models.DateTimeField(default=get_utcnow)

    version = models.CharField(max_length=25, default="1")

    identity = models.CharField(max_length=25)

    confirm_identity = models.CharField(max_length=25)

    dob = models.DateField(default=date(1995, 1, 1))


class Requisition(RequisitionModelMixin, BaseUuidModel):
    def update_reference_on_save(self):
        pass


class CrfOne(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfTwo(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfThree(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfFour(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfFive(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfSix(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class CrfSeven(CrfModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=50, default=uuid.uuid4)


class RedirectModel(BaseUuidModel):
    subject_identifier = models.CharField(max_length=25)


class RedirectNextModel(BaseUuidModel):
    subject_identifier = models.CharField(max_length=25)
