"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'demo_admin_tools_zinnia.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'demo_admin_tools_zinnia.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard import modules
from admin_tools.dashboard import Dashboard
from admin_tools.dashboard import AppIndexDashboard

from admin_tools_zinnia.modules.comments import Comments
from admin_tools_zinnia.modules.linkbacks import Linkbacks
from admin_tools_zinnia.modules.quick_entry import QuickEntry
from admin_tools_zinnia.modules.draft_entries import DraftEntries
from admin_tools_zinnia.modules.statistics import ZinniaStatistics

apps_group = modules.Group(
    title=_('Applications'),
    display='tabs',
    children=[
        modules.AppList(
            _('Weblog'),
            models=('zinnia.*', 'tagging.*',
                    'django.contrib.comments.*')
            ),
        modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
            exclude=('django.contrib.comments.*',)
            )]
    )


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for demo_admin_tools_zinnia.
    """
    columns = 3

    def init_with_context(self, context):
        self.children.append(apps_group)
        self.children.append(ZinniaStatistics())
        self.children.append(QuickEntry())
        self.children.append(DraftEntries())
        self.children.append(Comments())
        self.children.append(Linkbacks())
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))
        self.children.append(modules.LinkList(
            _('Zinnia support'),
            children=[
                {'title': _('Online documentation'),
                 'url': 'http://django-blog-zinnia.readthedocs.org/',
                 'external': True,
                 },
                {'title': _('Mailing list'),
                 'url': 'http://groups.google.com/group/django-blog-zinnia/',
                 'external': True,
                 },
                {'title': _('Issue tracker'),
                 'url': 'https://github.com/Fantomas42/django-blog-zinnia/issues',
                 'external': True,
                 }]
            ))
        self.children.append(modules.Feed(
            _('Recent commits on Zinnia'),
            feed_url='https://github.com/Fantomas42/django-blog-zinnia/commits/develop.atom',
            limit=5))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for demo_admin_tools_zinnia.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
