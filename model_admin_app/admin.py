from django import forms
from django.contrib import admin
from edc_crf.modelform_mixins import CrfModelFormMixin

from edc_model_admin.mixins import (
    ModelAdminNextUrlRedirectMixin,
    ModelAdminRedirectOnDeleteMixin,
    TemplatesModelAdminMixin,
)

from .models import (
    CrfFive,
    CrfFour,
    CrfOne,
    CrfSeven,
    CrfSix,
    CrfThree,
    CrfTwo,
    RedirectNextModel,
    Requisition,
)

__all__ = [
    "CrfOneAdmin",
    "RedirectNextModelAdmin",
    "CrfTwoAdmin",
    "CrfThreeAdmin",
    "RequisitionAdmin",
    "CrfFourAdmin",
    "CrfFiveAdmin",
    "CrfSixAdmin",
]

from edc_model_admin.dashboard import ModelAdminCrfDashboardMixin

from .admin_site import model_admin_app_admin


class BaseModelAdmin(TemplatesModelAdminMixin):
    search_fields = ("subject_identifier",)


@admin.register(CrfOne, site=model_admin_app_admin)
class CrfOneAdmin(BaseModelAdmin, admin.ModelAdmin):
    pass


# using ModelAdminNextUrlRedirectMixin


@admin.register(RedirectNextModel, site=model_admin_app_admin)
class RedirectNextModelAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    pass


@admin.register(CrfTwo, site=model_admin_app_admin)
class CrfTwoAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfThree, site=model_admin_app_admin)
class CrfThreeAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    pass


@admin.register(Requisition, site=model_admin_app_admin)
class RequisitionAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


# using ModelAdminRedirectOnDeleteMixin


@admin.register(CrfFour, site=model_admin_app_admin)
class CrfFourAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard_url"

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(CrfFive, site=model_admin_app_admin)
class CrfFiveAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard2_url"

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(CrfSix, site=model_admin_app_admin)
class CrfSixAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = None

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


class CrfSevenForm(CrfModelFormMixin, forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = CrfSeven


@admin.register(CrfSeven, site=model_admin_app_admin)
class CrfSevenAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = False

    form = CrfSevenForm
