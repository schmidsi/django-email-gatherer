#!/usr/bin/env python

from distutils.core import setup
import os
import setuplib

packages, package_data = setuplib.find_packages('email_gatherer')

setup(name='email_gatherer',
    version=__import__('email_gatherer').VERSION,
    description='One of the biggest goals of most of the websites is simply to gather emails. And here are the tools to do it right. (Hopefully) ',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read().decode('utf-8'),
    author='Simon Schmid',
    author_email='simon@schmidsi.ch',
    url='https://github.com/schmidsi/django-email-gatherer',
    license='BSD License',
    platforms=['OS Independent'],
    packages=packages,
    package_data=package_data,
)