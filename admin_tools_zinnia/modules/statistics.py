"""Statistics module for admin_tools_zinnia"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard.modules import DashboardModule


class ZinniaStatistics(DashboardModule):
    """Dashboard module for displaying Zinnia's statistics"""
    title = _('Today')
    template = 'admin_tools_zinnia/dashboard/modules/statistics.html'

    def is_empty(self):
        return False
