#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README-PYPI.rst')) as readme:
    README = readme.read()


setup(
    name='appsembler-apis',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',
    description='Appsembler APIs for Open edX',
    long_description=README,
    url='https://github.com/appsembler/appsembler-apis',
    author='Appsembler',
    author_email='opensource@appsembler.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    entry_points={
        'lms.djangoapp': [
            'appsembler_apis = appsembler_apis.apps.AppsemblerApisConfig',
        ]
    }
)