==================
Admin-tools Zinnia
==================

Admin-tools-zinnia is package providing new dashboard modules related to
your `Zinnia`_ application for `django-admin-tools`_.

.. _Zinnia: http://django-blog-zinnia.com/
.. _django-admin-tools: http://pypi.python.org/pypi/django-admin-tools/

Installation
============

* Install the package on your system: ::

  $ pip install django-admin-tools
  $ pip install admin-tools-zinnia

* Add the followings apps at the beginning of your ``INSTALLED_APPS``: ::

    INSTALLED_APPS = (
      'admin_tools',
      'admin_tools.theming',
      'admin_tools.menu',
      'admin_tools.dashboard',
      'admin_tools_zinnia',
      ...
    )
    
* Add ``admin_tools.urls`` before ``admin.site.urls`` to yours url file: ::

    urlpatterns = [
      ...
      url(r'^admin/tools/', include('admin_tools.urls')),
      url(r'^admin/', include(admin.site.urls)),
    ]

* Launch database migration: ::

  $ ./manage.py migrate


You are done !


