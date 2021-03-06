#!/usr/bin/env python
import os
import re
import sys

from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'xlib',
]

about = {}
with open(os.path.join(here, 'keylogger', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['A simple keylogger'],
    long_description=readme,
    author=about['Giacomo Lawrance'],
    author_email=about['thenerdystudent@gmail.com'],
    url=about['simple-keylogger.github.io'],
    install_requires=requires,
    license=about['MIT'],
    packages=find_packages(),
    zip_safe=False,
    entry_points = {
        'console_scripts':
        ["keylogger = keylogger.keylogger:main"],
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
