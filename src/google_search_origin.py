################################################################################
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Created Date: 21-09-14
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

import time
from typing import Any, List
import requests

import bs4

import src.common.yaml as google_serach_yaml

########################################################################################################################
#
# Const variables
#

GOOGLE_SEARCH_ORIGIN_SAFETY_OFF: int = 0
GOOGLE_SEARCH_ORIGIN_SAFETY_MEDIUM: int = 1
GOOGLE_SEARCH_ORIGIN_SAFETY_HIGH: int = 2

GOOGLE_SEARCH_ORIGIN_SITE_INCLUDE_INCLUDE: bool = True
GOOGLE_SEARCH_ORIGIN_SITE_INCLUDE_EXCLUDE: bool = False

GOOGLE_SEARCH_ORIGIN_FROM_DATE_DAY: str = 'day'
GOOGLE_SEARCH_ORIGIN_FROM_DATE_WEEK: str = 'week'
GOOGLE_SEARCH_ORIGIN_FROM_DATE_MONTH: str = 'month'
GOOGLE_SEARCH_ORIGIN_FROM_DATE_YEAR: str = 'year'


class GoogleSearchOrigin:
    ####################################################################################################################
    #
    # Const Google Search Origin variables
    #

    VERSION: str = '1.0.0'
    VERSION_DATE: str = '21/09/2021'
    PROGRAM_NAME: str = 'Google Search Origin'

    UNITTEST = False

    __key_filter__: str = 'filter'
    __path_filter__: str = 'src/configuration/filter.yaml'
    __key_tag_to_escape__: str = 'tag_to_escape'
    __key_escaping_character__: str = 'escaping_character'
    __path_escaping_character__: str = 'src/configuration/escaping_character.yaml'
    __key_character_encoding_schemes__: str = 'character_encoding_schemes'
    __path_character_encoding_schemes__: str = 'src/configuration/character_encoding_schemes.yaml'
    __key_country_collection_values__: str = 'country_collection_values'
    __path_country_collection_values__: str = 'src/configuration/country_collection_values.yaml'
    __key_supported_interface_languages__: str = 'supported_interface_languages'
    __path_supported_interface_languages__: str = 'src/configuration/supported_interface_languages.yaml'
    __key_language_collection_values__: str = 'language_collection_values'
    __path_language_collection_values__: str = 'src/configuration/language_collection_values.yaml'
    __key_country_codes__: str = 'country_codes'
    __path_country_codes__: str = 'src/configuration/country_codes.yaml'
    __key_picture_format__: str = 'picture_format'
    __key_picture_size__: str = 'picture_size'
    __key_picture_type__: str = 'picture_type'
    __key_picture_color_filter__: str = 'picture_color_filter'
    __key_picture_color__: str = 'picture_color'
    __key_picture_right__: str = 'picture_right'
    __path_picture__: str = 'src/configuration/picture.yaml'

    ####################################################################################################################
    #
    # Initialisation
    #

    def __init__(self, search_type: str = 'search', filter: str = None, base_url: str = 'www.google.com',
    ssl_certificate: bool = True, search: str = None, c2coff: bool = None, country: str = None,
    no_duplicate: bool = None, user_interface_language: str = None, and_operator: str = None,
    written_document_language: str = None, result_number: int = None, restrict_country: str = None, safety: int = None,
    start_page: int = None, site: str = None, site_include: bool = None, include_word: str = None,
    exclude_word: str = None, url_link: str = None, inclusive_search_range_start: int = None,
    inclusive_search_range_end: int = None, or_operator: str = None, additional_term: str = None,
    from_date: dict = None, related_url: str = None, client: str = None, search_engine_code: str = None,
    boost_country_search: str = None, character_encoding_scheme_interpreter: str = None,
    character_encoding_scheme_decoder: str = None, output_format: str = None, sort: str = None,
    idn_encoded_url: bool = None, picture_format: str = None, picture_size: str = None, picture_type: str = None,
    picture_color_filter: str = None, picture_color: str = None, picture_right: str = None, dorks_links: list = None,
    dorks_or: list = None, dorks_theme_exclusion: list = None, dorks_file_type_exclusion: list = None,
    dorks_file_type: list = None, dorks_and: list = None, dorks_words_in_links: list = None,
    dorks_should_appear: list = None, dorks_related_links: list = None, dorks_words_in_text: list = None,
    dorks_word_in_title: list = None, dorks_words_in_title: list = None, dorks_word_in_url: list = None,
    dorks_words_in_url: list = None, dorks_info: list = None, dorks_cache: list = None, dorks_anchor: list = None,
    dorks_define: list = None, dorks_stocks: list = None, dorks_phonebook: list = None, dorks_maps: list = None,
    dorks_book: list = None, dorks_movie: list = None, dorks_site: list = None, headers: dict = None,
    proxies: dict = None, cookies: dict = None, timeout: int = None, allow_redirects: bool = None,
    verify: Any = True, certificate: str = None, request_cooldown: float = None):
        self.configuration = {}

        self.url: str = None
        self.base_url: str = None
        self.search_type: str = None
        self.protocol: str = None
        self.url_parameters: dict = {}
        self.dorks: dict = {}

        self.headers: dict = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/61.0.3163.100 Safari/537.36'}
        self.cookies: dict = {}
        self.timeout: int = None
        self.allow_redirects: bool = None
        self.proxies: dict = {}
        self.verify: bool = None
        self.certificate: str = None
        self.request_cooldown: float = 0
        self.last_request: time = None

        self.is_google_violated: bool = False

        self.response = None

        self.import_configuration(self.__path_escaping_character__)

        self.parameter_headers(headers)
        self.parameter_cookies(cookies)
        self.parameter_timeout(timeout)
        self.parameter_allow_redirects(allow_redirects)
        self.parameter_proxies(proxies)
        self.parameter_verify(verify)
        self.parameter_certificate(certificate)
        self.parameter_request_cooldown(request_cooldown)

        self.parameter_search_type(search_type)
        self.parameter_filter(filter)
        self.parameter_base_url(base_url)
        self.parameter_ssl_certificate(ssl_certificate)
        self.parameter_search(search)
        self.parameter_c2coff(c2coff)
        self.parameter_country('cr', country)
        self.parameter_no_duplicate(no_duplicate)
        self.parameter_language('hl', user_interface_language)
        self.parameter_and_operator(and_operator)
        self.parameter_written_document_language(written_document_language)
        self.parameter_result_number(result_number)
        self.parameter_country('restrict', restrict_country)
        self.parameter_safety(safety)
        self.parameter_start_page(start_page)
        self.parameter_site(site)
        self.parameter_site_include(site_include)
        self.parameter_include_word(include_word)
        self.parameter_exclude_word(exclude_word)
        self.parameter_url_link(url_link)
        self.parameter_inclusive_search_range_start(inclusive_search_range_start)
        self.parameter_inclusive_search_range_end(inclusive_search_range_end)
        self.parameter_or_operator(or_operator)
        self.parameter_additional_term(additional_term)
        self.parameter_from_date(from_date)
        self.parameter_related_url(related_url)
        self.parameter_client(client)
        self.parameter_search_engine_code(search_engine_code)
        self.parameter_language('gl', boost_country_search)
        self.parameter_character_encoding_scheme_interpreter(character_encoding_scheme_interpreter)
        self.parameter_character_encoding_scheme_decoder(character_encoding_scheme_decoder)
        self.parameter_output_format(output_format)
        self.parameter_sort(sort)
        self.parameter_idn_encoded_url(idn_encoded_url)
        self.parameter_picture_format(picture_format)
        self.parameter_picture_size(picture_size)
        self.parameter_picture_type(picture_type)
        self.parameter_picture_color_filter(picture_color_filter)
        self.parameter_picture_color(picture_color)
        self.parameter_picture_right(picture_right)
        self.parameter_dorks_links(dorks_links)
        self.parameter_dorks_or(dorks_or)
        self.parameter_dorks_theme_exclusion(dorks_theme_exclusion)
        self.parameter_dorks_file_type_exclusion(dorks_file_type_exclusion)
        self.parameter_dorks_file_type(dorks_file_type)
        self.parameter_dorks_and(dorks_and)
        self.parameter_dorks_words_in_links(dorks_words_in_links)
        self.parameter_dorks_should_appear(dorks_should_appear)
        self.parameter_dorks_related_links(dorks_related_links)
        self.parameter_dorks_words_in_text(dorks_words_in_text)
        self.parameter_dorks_word_in_title(dorks_word_in_title)
        self.parameter_dorks_words_in_title(dorks_words_in_title)
        self.parameter_dorks_word_in_url(dorks_word_in_url)
        self.parameter_dorks_words_in_url(dorks_words_in_url)
        self.parameter_dorks_info(dorks_info)
        self.parameter_dorks_cache(dorks_cache)
        self.parameter_dorks_anchor(dorks_anchor)
        self.parameter_dorks_define(dorks_define)
        self.parameter_dorks_stocks(dorks_stocks)
        self.parameter_dorks_phonebook(dorks_phonebook)
        self.parameter_dorks_maps(dorks_maps)
        self.parameter_dorks_book(dorks_book)
        self.parameter_dorks_movie(dorks_movie)
        self.parameter_dorks_site(dorks_site)

        self.assemble_url()

    def import_configuration(self, path: str) -> None:
        self.configuration.update(google_serach_yaml.Yaml().read_yaml(path))

    def request_url(self):
        if (not self.is_google_violated and
        (not self.last_request or time.time() - self.last_request >= self.request_cooldown)):
            self.last_request = time.time()
            self.response = requests.get(url=self.url, headers=self.headers, cookies=self.cookies, timeout=self.timeout,
            allow_redirects=self.allow_redirects, proxies=self.proxies, verify=self.verify, cert=self.certificate)
            if (self.response.status_code == 429):
                self.is_google_violated = True
        else:
            self.response = None

    ####################################################################################################################
    #
    # Getters
    #

    def get_all_links(self) -> None:
        if (self.get_response_is_ok()):
            all_links = []
            parsed_response = bs4.BeautifulSoup(self.get_response_text(), 'html.parser').find_all(
            'div', attrs={'class': 'g'})
            for div in parsed_response:
                link = div.find('a', href=True)
                title = div.find('h3')
                if (link and title):
                    all_links.append(link['href'])
        return all_links

    def get_response_status(self) -> int:
        if (self.response):
            return self.response.status_code

    def get_response_text(self) -> str:
        if (self.response):
            return self.response.text
    
    def get_apparent_encoding(self) -> str:
        if (self.response):
            return self.response.apparent_encoding

    def get_response_is_permanent_redirect(self) -> str:
        if (self.response):
            return self.response.is_permanent_redirect
    
    def get_response_is_redirect(self) -> str:
        if (self.response):
            return self.response.is_redirect
    
    def get_response_links(self) -> str:
        if (self.response):
            return self.response.links

    def get_response_is_ok(self) -> str:
        if (self.response):
            return self.response.ok
    
    def get_response_text(self) -> str:
        if (self.response):
            return self.response.text

    def get_reponse_raw(self) -> str:
        if (self.response):
            return self.response.raw

    ####################################################################################################################
    #
    # Setup request parameters
    #

    def parameter_headers(self, headers: dict) -> None:
        if (headers):
            self.headers = headers

    def parameter_cookies(self, cookies: dict) -> None:
        if (cookies):
            self.cookies = cookies

    def parameter_timeout(self, timeout: int) -> None:
        self.timeout = timeout

    def parameter_allow_redirects(self, allow_redirects: bool) -> None:
        if (allow_redirects != None):
            self.allow_redirects = allow_redirects

    def parameter_proxies(self, proxies: str) -> None:
        if (proxies):
            self.proxies = proxies

    def parameter_verify(self, verify: Any) -> None:
        self.verify = verify
    
    def parameter_certificate(self, certificate: str) -> None:
        self.certificate = certificate

    def parameter_request_cooldown(self, request_cooldown: int) -> None:
        if (request_cooldown):
            self.request_cooldown = request_cooldown
        else:
            self.request_cooldown = 0

    ####################################################################################################################
    #
    # Setup URL parameters
    #

    def parameter_search_type(self, search_type: str) -> None:
        if (search_type):
            self.search_type = search_type
        else:
            self.search_type = 'search'

    def parameter_filter(self, filter: str) -> None:
        if (filter):
            if (self.__key_filter__ not in self.configuration):
                self.import_configuration(self.__path_filter__)
            
            if (filter in self.configuration[self.__key_filter__]):
                self.url_parameters['tbm'] = filter

    def parameter_base_url(self, base_url: str) -> None:
        if (base_url):
            self.base_url = base_url
        else:
            self.base_url = 'www.google.com'

    def parameter_ssl_certificate(self, ssl_certificate: bool) -> None:
        if (ssl_certificate != None):
            if (ssl_certificate):
                self.protocol = 'https'
            else:
                self.protocol = 'http'

    def parameter_search(self, search: str) -> None:
        if (search):
            self.url_parameters['q'] = search


    def parameter_c2coff(self, c2coff: bool) -> None:
        if (c2coff != None):
            if (c2coff):
                self.url_parameters['c2coff'] = '2'
            else:
                self.url_parameters['c2coff'] = '1'


    def parameter_country(self, tag: str, country: str) -> None:
        if (country):
            if (not self.__key_country_collection_values__ in self.configuration):
                self.import_configuration(self.__path_country_collection_values__)

            if (len(country) == 2):
                if (not country.isupper()):
                    country = f'country{country.upper()}'
                else:
                    country = f'country{country}'
            if (len(country) == 9):
                if (not country[:7].islower() or not country[7:].isupper()):
                    country = f'{country[:7].lower()}{country[7:].upper()}'
            if (country in self.configuration[self.__key_country_collection_values__]):
                self.url_parameters[tag] = country


    def parameter_no_duplicate(self, no_duplicate: bool) -> None:
        if (no_duplicate != None):
            if (no_duplicate):
                self.url_parameters['filter'] = '0'
            else:
                self.url_parameters['filter'] = '1'

    def parameter_language(self, tag: str, language: str) -> None:
        if (language):
            if (tag == 'gl' and not self.__key_country_codes__ in self.configuration):
                self.import_configuration(self.__path_country_codes__)
            if (tag == 'hl' and not self.__key_supported_interface_languages__ in self.configuration):
                self.import_configuration(self.__path_supported_interface_languages__)

            if (len(language) == 2):
                if (not language.islower()):
                    language = language.lower()
            else:
                splited_language = language.split('-')
                if (len(splited_language) == 2):
                    if (not splited_language[0].islower() or
                    not splited_language[1].isupper()):
                        language = (f'{splited_language[0].lower()}-'
                        f'{splited_language[1].upper()}')
                else:
                    return
            if ((tag == 'gl' and language in self.configuration[self.__key_country_codes__]) or
            (tag == 'hl' and language in self.configuration[self.__key_supported_interface_languages__])):
                self.url_parameters[tag] = language

    def parameter_and_operator(self, and_operator: str):
        if (and_operator):
            self.url_parameters['hq'] = and_operator

    def parameter_written_document_language(self, written_document_language: str) -> None:
        if (written_document_language):
            if (not self.__key_language_collection_values__ in self.configuration):
                self.import_configuration(self.__path_language_collection_values__)

            if (len(written_document_language) == 7):
                if (not written_document_language.islower()):
                    written_document_language = written_document_language.lower()
            else:
                splited_written_document_language = written_document_language.split('-')
                if (len(splited_written_document_language) == 2):
                    if (not splited_written_document_language[0].islower() or
                    not splited_written_document_language[1].isupper()):
                        written_document_language = (f'{splited_written_document_language[0].lower()}'
                        f'-{splited_written_document_language[1].upper()}')
                else:
                    return
            if (written_document_language in self.configuration[self.__key_language_collection_values__]):
                self.url_parameters['lr'] = written_document_language

    def parameter_result_number(self, result_number: int) -> None:
        if (result_number != None and result_number > 0):
            self.url_parameters['num'] = result_number

    def parameter_safety(self, safety: int) -> None:
        if (safety != None):
            if (safety == 0):
                self.url_parameters['safe'] = 'off'
            elif (safety == 1):
                self.url_parameters['safe'] = 'medium'
            elif (safety == 2):
                self.url_parameters['safe'] = 'high'

    def parameter_start_page(self, start_page: int) -> None:
        if (start_page != None and start_page > 0):
            self.url_parameters['start'] = start_page

    def parameter_site(self, site: str) -> None:
        if (site):
            self.url_parameters['as_sitesearch'] = site
    
    def parameter_site_include(self, site_include: bool) -> None:
        if (site_include != None):
            if (site_include):
                self.url_parameters['as_dt'] = 'i'
            else:
                self.url_parameters['as_dt'] = 'e'
    
    def parameter_include_word(self, include_word: str) -> None:
        if (include_word):
            self.url_parameters['as_epq'] = include_word

    def parameter_exclude_word(self, exclude_word: str) -> None:
        if (exclude_word):
            self.url_parameters['as_eq'] = exclude_word

    def parameter_url_link(self, url_link: str) -> None:
        if (url_link):
            self.url_parameters['as_lq'] = url_link

    def parameter_inclusive_search_range_start(self, inclusive_search_range_start: int) -> None:
        if (inclusive_search_range_start != None and inclusive_search_range_start > 0):
            self.url_parameters['as_nlo'] = inclusive_search_range_start
    
    def parameter_inclusive_search_range_end(self, inclusive_search_range_end: int) -> None:
        if (inclusive_search_range_end != None and inclusive_search_range_end > 0):
            self.url_parameters['as_nhi'] = inclusive_search_range_end

    def parameter_or_operator(self, or_operator: str) -> None:
        if (or_operator):
            self.url_parameters['as_oq'] = or_operator
    
    def parameter_additional_term(self, additional_term: str) -> None:
        if (additional_term):
            self.url_parameters['as_q'] = additional_term

    def parameter_from_date(self, from_date: dict) -> None:
        if (from_date):
            if (GOOGLE_SEARCH_ORIGIN_FROM_DATE_DAY in from_date and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_DAY] and
            from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_DAY] >= 0):
                self.url_parameters['as_qdr'] = f'd{from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_DAY]}'
            elif (GOOGLE_SEARCH_ORIGIN_FROM_DATE_WEEK in from_date and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_WEEK]
            and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_WEEK] >= 0):
                self.url_parameters['as_qdr'] = f'w{from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_WEEK]}'
            elif (GOOGLE_SEARCH_ORIGIN_FROM_DATE_MONTH in from_date and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_MONTH]
            and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_MONTH] >= 0):
                self.url_parameters['as_qdr'] = f'm{from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_MONTH]}'
            elif (GOOGLE_SEARCH_ORIGIN_FROM_DATE_YEAR in from_date and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_YEAR]
            and from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_YEAR] >= 0):
                self.url_parameters['as_qdr'] = f'y{from_date[GOOGLE_SEARCH_ORIGIN_FROM_DATE_YEAR]}'

    def parameter_related_url(self, related_url: str) -> None:
        if (related_url):
            self.url_parameters['as_rq'] = related_url

    def parameter_client(self, client: str) -> None:
        if (client):
            self.url_parameters['client'] = client
    
    def parameter_search_engine_code(self, search_engine_code: str) -> None:
        if (search_engine_code):
            self.url_parameters['cx'] = search_engine_code

    def parameter_character_encoding_scheme_interpreter(self, character_encoding_scheme: str) -> None:
        if (character_encoding_scheme):
            if (not self.__key_character_encoding_schemes__ in self.configuration):
                self.import_configuration(self.__path_character_encoding_schemes__)

            if (not character_encoding_scheme.islower()):
                character_encoding_scheme = character_encoding_scheme.lower()
            if (character_encoding_scheme in self.configuration[self.__key_character_encoding_schemes__]):
                self.url_parameters['ie'] = character_encoding_scheme

    def parameter_character_encoding_scheme_decoder(self, character_encoding_scheme_decoder:str ) -> None:
        if (character_encoding_scheme_decoder):
            if (not self.__key_character_encoding_schemes__ in self.configuration):
                self.import_configuration(self.__path_character_encoding_schemes__)

            if (not character_encoding_scheme_decoder.islower()):
                character_encoding_scheme_decoder = character_encoding_scheme_decoder.lower()
            if (character_encoding_scheme_decoder in self.configuration[self.__key_character_encoding_schemes__]):
                self.url_parameters['oe'] = character_encoding_scheme_decoder

    def parameter_output_format(self, output_format: str) -> None:
        if (output_format and output_format in ['xml_no_dtd', 'xml']):
            self.url_parameters['output'] = output_format

    def parameter_sort(self, sort: str) -> None:
        if (sort):
            self.url_parameters['sort'] = sort
    
    def parameter_idn_encoded_url(self, idn_encoded_url: bool) -> None:
        if (idn_encoded_url != None):
            if (idn_encoded_url):
                self.url_parameters['ud'] = '1'
            else:
                self.url_parameters['ud'] = '0'

    def parameter_picture_format(self, picture_format: str) -> None:
        if (picture_format):
            if (not self.__key_picture_format__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_format.islower()):
                picture_format = picture_format.lower()
            if (picture_format in self.configuration[self.__key_picture_format__]):
                 self.url_parameters['as_filetype'] = picture_format
    
    def parameter_picture_size(self, picture_size: str) -> None:
        if (picture_size):
            if (not self.__key_picture_size__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_size.islower()):
                picture_size = picture_size.lower()
            if (picture_size in self.configuration[self.__key_picture_size__]):
                 self.url_parameters['imgsz'] = picture_size
    
    def parameter_picture_type(self, picture_type: str) -> None:
        if (picture_type):
            if (not self.__key_picture_type__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_type.islower()):
                picture_type = picture_type.lower()
            if (picture_type in self.configuration[self.__key_picture_type__]):
                 self.url_parameters['imgtype'] = picture_type
    
    def parameter_picture_color_filter(self, picture_color_filter: str) -> None:
        if (picture_color_filter):
            if (not self.__key_picture_color_filter__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_color_filter.islower()):
                picture_color_filter = picture_color_filter.lower()
            if (picture_color_filter in self.configuration[self.__key_picture_color_filter__]):
                 self.url_parameters['imgc'] = picture_color_filter
    
    def parameter_picture_color(self, picture_color: str) -> None:
        if (picture_color):
            if (not self.__key_picture_color__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_color.islower()):
                picture_color = picture_color.lower()
            if (picture_color in self.configuration[self.__key_picture_color__]):
                 self.url_parameters['imgcolor'] = picture_color
    
    def parameter_picture_right(self, picture_right: str) -> None:
        if (picture_right):
            if (not self.__key_picture_right__ in self.configuration):
                self.import_configuration(self.__path_picture__)
            if (not picture_right.islower()):
                picture_right = picture_right.lower()
            if (picture_right in self.configuration[self.__key_picture_right__]):
                 self.url_parameters['as_rights'] = picture_right

    def parameter_dorks_links(self, dorks_links: list) -> None:
        if (dorks_links):
            for index in range(len(dorks_links)):
                dorks_links[index] = f'link:{dorks_links[index]}'
            self.dorks['link'] = ' '.join(dorks_links)
    
    def parameter_dorks_or(self, dorks_or: list) -> None:
        if (dorks_or):
            self.dorks['or'] = ' OR '.join(dorks_or)
    
    def parameter_dorks_theme_exclusion(self, dorks_theme_exclusion: list) -> None:
        if (dorks_theme_exclusion):
            for index in range(len(dorks_theme_exclusion)):
                dorks_theme_exclusion[index] = f'-{dorks_theme_exclusion[index]}'
            self.dorks['-'] = ' '.join(dorks_theme_exclusion)
    
    def parameter_dorks_file_type_exclusion(self, dorks_file_type_exclusion: list) -> None:
        if (dorks_file_type_exclusion):
            for index in range(len(dorks_file_type_exclusion)):
                dorks_file_type_exclusion[index] = f'-filetype:{dorks_file_type_exclusion[index]}'
            self.dorks['-filetype'] = ' '.join(dorks_file_type_exclusion)

    def parameter_dorks_file_type(self, dorks_file_type: list) -> None:
        if (dorks_file_type):
            for index in range(len(dorks_file_type)):
                dorks_file_type[index] = f'filetype:{dorks_file_type[index]}'
            self.dorks['filetype'] = ' '.join(dorks_file_type)

    def parameter_dorks_and(self, dorks_and: list) -> None:
        if (dorks_and):
            self.dorks['+'] = '+'.join(dorks_and)
    
    def parameter_dorks_words_in_links(self, dorks_words_in_links: list) -> None:
        if (dorks_words_in_links):
            for index in range(len(dorks_words_in_links)):
                dorks_words_in_links[index] = f'allinlinks:{dorks_words_in_links[index]}'
            self.dorks['allinlinks'] = ' '.join(dorks_words_in_links)
    
    def parameter_dorks_should_appear(self, dorks_should_appear: list) -> None:
        if (dorks_should_appear):
            for index in range(len(dorks_should_appear)):
                dorks_should_appear[index] = f'"{dorks_should_appear[index]}"'
            self.dorks['""'] = ' '.join(dorks_should_appear)
    
    def parameter_dorks_related_links(self, dorks_related_links: list) -> None:
        if (dorks_related_links):
            for index in range(len(dorks_related_links)):
                dorks_related_links[index] = f'related:{dorks_related_links[index]}'
            self.dorks['related'] = ' '.join(dorks_related_links)
    
    def parameter_dorks_words_in_text(self, dorks_words_in_text: list) -> None:
        if (dorks_words_in_text):
            for index in range(len(dorks_words_in_text)):
                dorks_words_in_text[index] = f'allintext:{dorks_words_in_text[index]}'
            self.dorks['allintext'] = ' '.join(dorks_words_in_text)
    
    def parameter_dorks_word_in_title(self, dorks_word_in_title: list) -> None:
        if (dorks_word_in_title):
            for index in range(len(dorks_word_in_title)):
                dorks_word_in_title[index] = f'intitle:{dorks_word_in_title[index]}'
            self.dorks['intitle'] = ' '.join(dorks_word_in_title)
        
    def parameter_dorks_words_in_title(self, dorks_words_in_title: list) -> None:
        if (dorks_words_in_title):
            for index in range(len(dorks_words_in_title)):
                dorks_words_in_title[index] = f'allintitle:{dorks_words_in_title[index]}'
            self.dorks['allintitle'] = ' '.join(dorks_words_in_title)
    
    def parameter_dorks_word_in_url(self, dorks_word_in_url: list) -> None:
        if (dorks_word_in_url):
            for index in range(len(dorks_word_in_url)):
                dorks_word_in_url[index] = f'inurl:{dorks_word_in_url[index]}'
            self.dorks['inurl'] = ' '.join(dorks_word_in_url)
    
    def parameter_dorks_words_in_url(self, dorks_words_in_url: list) -> None:
        if (dorks_words_in_url):
            for index in range(len(dorks_words_in_url)):
                dorks_words_in_url[index] = f'allinurl:{dorks_words_in_url[index]}'
            self.dorks['allinurl'] = ' '.join(dorks_words_in_url)
    
    def parameter_dorks_info(self, dorks_info: list) -> None:
        if (dorks_info):
            for index in range(len(dorks_info)):
                dorks_info[index] = f'info:{dorks_info[index]}'
            self.dorks['info'] = ' '.join(dorks_info)
    
    def parameter_dorks_cache(self, dorks_cache: list) -> None:
        if (dorks_cache):
            for index in range(len(dorks_cache)):
                dorks_cache[index] = f'cache:{dorks_cache[index]}'
            self.dorks['cache'] = ' '.join(dorks_cache)
    
    def parameter_dorks_anchor(self, dorks_anchor: list) -> None:
        if (dorks_anchor):
            for index in range(len(dorks_anchor)):
                dorks_anchor[index] = f'inanchor:{dorks_anchor[index]}'
            self.dorks['inanchor'] = ' '.join(dorks_anchor)

    def parameter_dorks_define(self, dorks_define: list) -> None:
        if (dorks_define):
            for index in range(len(dorks_define)):
                dorks_define[index] = f'define:{dorks_define[index]}'
            self.dorks['define'] = ' '.join(dorks_define)

    def parameter_dorks_stocks(self, dorks_stocks: list) -> None:
        if (dorks_stocks):
            for index in range(len(dorks_stocks)):
                dorks_stocks[index] = f'stocks:{dorks_stocks[index]}'
            self.dorks['stocks'] = ' '.join(dorks_stocks)

    def parameter_dorks_phonebook(self, dorks_phonebook: list) -> None:
        if (dorks_phonebook):
            for index in range(len(dorks_phonebook)):
                dorks_phonebook[index] = f'phonebook:{dorks_phonebook[index]}'
            self.dorks['phonebook'] = ' '.join(dorks_phonebook)
    
    def parameter_dorks_maps(self, dorks_maps: list) -> None:
        if (dorks_maps):
            for index in range(len(dorks_maps)):
                dorks_maps[index] = f'maps:{dorks_maps[index]}'
            self.dorks['maps'] = ' '.join(dorks_maps)
    
    def parameter_dorks_book(self, dorks_book: list) -> None:
        if (dorks_book):
            for index in range(len(dorks_book)):
                dorks_book[index] = f'book:{dorks_book[index]}'
            self.dorks['book'] = ' '.join(dorks_book)
    
    def parameter_dorks_movie(self, dorks_movie: list) -> None:
        if (dorks_movie):
            for index in range(len(dorks_movie)):
                dorks_movie[index] = f'movie:{dorks_movie[index]}'
            self.dorks['movie'] = ' '.join(dorks_movie)

    def parameter_dorks_site(self, dorks_site: list) -> None:
        if (dorks_site):
            for index in range(len(dorks_site)):
                dorks_site[index] = f'site:{dorks_site[index]}'
            self.dorks['site'] = ' '.join(dorks_site)

    ####################################################################################################################
    #
    # Assemble
    #

    def assemble_url(self) -> None:
        self.url = self.base_url
        if (self.protocol != None):
            self.url = '{protocol}://{url}'.format(protocol=self.protocol, url=self.url)
        if (self.url_parameters != {} or self.dorks != {}):
            self.url = '{url_prefix}/{search_type}?{url_parameters}'.format(url_prefix=self.url,
            search_type=self.search_type, url_parameters=self.encode_url(self.url_parameters))

    def encode_url(self, parameters: dict) -> str:
        encoded_url = ''
        if (self.dorks):
            if ('q' in parameters):
                parameters['q'] = f'{" ".join(self.dorks.values())} {parameters["q"]}'
            else:
                parameters['q'] = f'{" ".join(self.dorks.values())}'
        for to_escape_tag in self.configuration[self.__key_tag_to_escape__]:
            if (to_escape_tag in parameters):
                for to_escape_character in self.configuration[self.__key_escaping_character__]:
                    parameters[to_escape_tag] = parameters[to_escape_tag].replace(to_escape_character,
                    self.configuration[self.__key_escaping_character__][to_escape_character])

        for tag, value in parameters.items():
            encoded_url = f'{encoded_url}&{tag}={value}'

        if (encoded_url):
            return encoded_url[1:]
        return ''

    ####################################################################################################################
    #
    # Getter
    #

    def get_url(self) -> str:
        return self.url

    ####################################################################################################################
    #
    # Cleaner
    #

    def clear_url_parameters(self) -> None:
        self.url_parameters = {}