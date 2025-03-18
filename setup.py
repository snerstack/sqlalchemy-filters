# -*- coding: utf-8 -*-

import os
from codecs import open
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r', 'utf-8') as handle:
    readme = handle.read()

setup(
    name='sqlalchemy-filters',
    version='0.13.0+rb6',
    description='A library to filter SQLAlchemy queries.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Student.com',
    author_email='wearehiring@student.com',
    url='https://github.com/juliotrigo/sqlalchemy-filters',
    packages=find_packages(exclude=['test', 'test.*']),
    python_requires='>=3.10',
    install_requires=['sqlalchemy>=1.4.0', 'six>=1.17.0'],
    extras_require={
        'dev': [
            'pytest>=8.3.5',
            'coverage~=7.7.0',
            'sqlalchemy-utils>=0.41.2',
            'flake8',
            'restructuredtext-lint',
            'Pygments',
            'coverage-conditional-plugin',
        ],
        'mysql': ['mysql-connector-python-rf==2.2.2'],
        'postgresql': ['psycopg2==2.9.10'],
    },
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
