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

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='google-search-origin',
    version='1.0.0',
    author='Da2ny',
    author_email='da2nydeveloper@gmail.com',
    description='Google Search Origin is used to search efficacy on Google. It is also used to scrap URL from google',
    long_description=('Google Search Origin encapsulate Request and BeautifulSoap libraries to collect data from the internet.'
    'It can generate url throught data passed as parameter. Its main functionnality would be for scraping'),
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