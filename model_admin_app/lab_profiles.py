from edc_lab import (
    AliquotType,
    LabProfile,
    ProcessingProfile,
    RequisitionPanel,
    site_labs,
)

wb = AliquotType(name="Whole Blood", alpha_code="WB", numeric_code="02")


fbc_processing = ProcessingProfile(name="FBC", aliquot_type=wb)

panel_one = RequisitionPanel(name="one", verbose_name="One", processing_profile=fbc_processing)

panel_two = RequisitionPanel(name="two", verbose_name="Two", processing_profile=fbc_processing)

lab_profile = LabProfile(name="lab_profile", requisition_model="model_admin_app.requisition")

lab_profile.add_panel(panel_one)
lab_profile.add_panel(panel_two)
site_labs.register(lab_profile=lab_profile)
