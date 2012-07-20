"""Linkbacks module for admin_tools_zinnia"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard.modules import DashboardModule


class Linkbacks(DashboardModule):
    """Dashboard module for displaying latest linkbacks"""
    title = _('Recent linkbacks')
    template = 'admin_tools_zinnia/dashboard/modules/linkbacks.html'

    # TODO implement limit

    def is_empty(self):
        return False
