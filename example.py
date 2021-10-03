################################################################################
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Created Date: 21-10-03
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

import google_search_origin


if __name__ == '__main__':
    # Initialisation of the class
    google_search = google_search_origin.GoogleSearchOrigin(search='sun')
    
    # Request from the url assembled
    google_search.request_url()

    # Display the link parsed depending on the result
    print(google_search.get_all_links())

    # Modify the parameter
    google_search.parameter_search('dog')

    # Assemble the url
    google_search.assemble_url()

    # Request from the url assembled
    google_search.request_url()

    # Display the raw text depending on the result
    print(google_search.get_response_text())
