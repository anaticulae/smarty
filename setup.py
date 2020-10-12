#!/usr/bin/env python
# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import re

import setuptools

ROOT = os.path.abspath(os.path.dirname(__file__))


def read(file):
    with open(file, mode='rt', encoding='utf8') as fp:
        return fp.read()


README = read(os.path.join(ROOT, 'README.md'))

VERSION = read(os.path.join(ROOT, 'smarty/__init__.py'))
VERSION = re.search(r'__version__ = \'(.*?)\'', VERSION).group(1)

INSTALL_REQUIRES = read(os.path.join(ROOT, "requirements.txt"))
INSTALL_REQUIRES = [
    line for line in INSTALL_REQUIRES.splitlines() if line and '#' not in line
]

if __name__ == "__main__":
    # allow ssetup.py to run from another directory
    os.chdir(ROOT)
    setuptools.setup(
        author='Helmut Konrad Fahrendholz',
        author_email='info@checkitweg.de',
        description='i am sooo smart',
        install_requires=INSTALL_REQUIRES,
        long_description=README,
        name='smarty',
        platforms='any',
        url='https://dev.package.checkitweg.de/smarty',
        version=VERSION,
        zip_safe=False,  # create 'zip'-file if True. Don't do it!
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        packages=[
            'smarty',
            'smarty.cli',
        ],
        entry_points={
            'console_scripts': ['smarty = smarty.cli:main'],
        },
    )
