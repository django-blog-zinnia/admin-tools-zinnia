"""Comments module for admin_tools_zinnia"""
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard.modules import DashboardModule


class Comments(DashboardModule):
    """Dashboard module for displaying latest comments"""
    title = _('Recent comments')
    template = 'admin_tools_zinnia/dashboard/modules/comments.html'

    # TODO implement limit

    def is_empty(self):
        return False
