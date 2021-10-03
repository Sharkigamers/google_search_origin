################################################################################
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Created Date: 21-09-21
# Author: Gabriel Danjon
# -----
# Last Modified: 
# Modified By: 
# -----
# Copyright (c) 2021 Da2ny's world
# 
# A clean code for a better programming
# -----
################################################################################

from genericpath import isfile
from os import path
import setuptools

def get_version(relpath):
    """read version info from file without importing it"""
    from os.path import dirname, join
    file_path = join(dirname(__file__), join('src', relpath))
    if (path.isfile(file_path)):
        for line in open(file_path, 'r'):
            if 'VERSION: str = ' in line:
                if '"' in line:
                    # VERSION: str = '1.0.0'
                    return line.split('"')[1]
                elif "'" in line:
                    return line.split('\'')[1]

def get_long_description():
  long_description = ''
  with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
  return long_description

setuptools.setup(
    name='google-search-origin',
    version=get_version('google_search_origin.py'),
    author='Da2ny',
    author_email='da2nydeveloper@gmail.com',
    description='Google Search Origin is used to search efficacy on Google. It is also used to scrap URL from google',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sharkigamers/google_search_origin',
    project_urls={
        'Bug Tracker': 'https://github.com/Sharkigamers/google_search_origin/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)