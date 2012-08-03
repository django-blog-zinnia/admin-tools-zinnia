"""Quick entry module for admin_tools_zinnia"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard.modules import DashboardModule


class QuickEntry(DashboardModule):
    """Dashboard module for quick publishing an entry"""
    title = _('Quick entry')
    template = 'admin_tools_zinnia/dashboard/modules/quick_entry.html'

    # TODO implement tag autocompletion

    def is_empty(self):
        return False
