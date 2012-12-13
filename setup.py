#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-punchclock',
    version=__import__('punchclock').__version__,

    requires = ['python (>= 2.5)', 'django (>= 1.2)'],
    provides = ['punchclock'],

    description='Middleware for separately logging requests and responses '
                'in order to help find crashed requests.',

    url='http://github.com/mivanov/django-punchclock',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,

    classifiers  = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
