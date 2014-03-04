"""Setup script for admin-tools-zinnia"""
from setuptools import setup
from setuptools import find_packages

import admin_tools_zinnia

setup(
    name='admin-tools-zinnia',
    version=admin_tools_zinnia.__version__,

    description='Admin tools for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, admin, dashboard',

    author=admin_tools_zinnia.__author__,
    author_email=admin_tools_zinnia.__email__,
    url=admin_tools_zinnia.__url__,

    packages=find_packages(exclude=['demo_admin_tools_zinnia']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=admin_tools_zinnia.__license__,
    include_package_data=True,
    zip_safe=False
)
