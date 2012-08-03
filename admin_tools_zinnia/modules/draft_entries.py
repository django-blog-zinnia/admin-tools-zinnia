"""Draft entries module for admin_tools_zinnia"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard.modules import DashboardModule


class DraftEntries(DashboardModule):
    """Dashboard module for displaying entries in draft status"""
    title = _('Draft entries')
    template = 'admin_tools_zinnia/dashboard/modules/draft_entries.html'

    # TODO implement limit

    def is_empty(self):
        return False
