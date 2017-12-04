#!/usr/bin/env python
# coding: utf-8

import io
import os
from setuptools import setup, find_packages


readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name     = 'pymailcloud',
    version  = '0.1',
    packages = find_packages(),

    install_requires = ['requests', 'requests-toolbelt', 'tqdm'],

    # in case you want to use slugify() with support for transliteration:
    description  = 'Unofficial python library for making API requests to [Cloud@Mail.ru](http://cloud.mail.ru/)',
    long_description = readme,
    author       = 'Alexey Gusev',
    author_email = 'gusev@aesc.msu.ru',
    url          = 'https://github.com/vladimirdotk/PyMailCloud',
    download_url = 'https://github.com/vladimirdotk/PyMailCloud/archive/master.zip',
    license      = 'GNU Lesser General Public License (LGPL), Version 3',
    keywords     = 'mail.ru cloud',
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)