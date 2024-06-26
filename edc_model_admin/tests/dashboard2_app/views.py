from edc_dashboard.view_mixins import EdcViewMixin
from edc_dashboard.views import DashboardView as BaseDashboardView


class DashboardView(EdcViewMixin, BaseDashboardView):
    dashboard_url_name = "dashboard2_url"
    dashboard_template = "dashboard2_template"
