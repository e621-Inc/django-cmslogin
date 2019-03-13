# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages


try:
    from pypandoc import convert
except ImportError:
    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


DESCRIPTION = 'Django CMS Login/Logout forms, cms_plugins and tags'

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 3 - Alpha',
]


setup(
    name='django-cmslogin',
    version='0.0.1',
    author='Alaric Mägerle',
    author_email='info@rouxcode.ch',
    description=DESCRIPTION,
    long_description=convert('README.md', 'rst'),
    url='https://github.com/rouxcode/django-cmslogin',
    license='MIT',
    keywords=['django'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django>=1.9'
    ],
    packages=find_packages(exclude=['example', 'docs']),
    include_package_data=True,
    zip_safe=False,
)
