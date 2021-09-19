from typing import Any, List
import requests

import src.common.yaml as google_serach_yaml


####################################################################################################################
#
# Const variables
#

SAFETY_OFF: int = 0
SAFETY_MEDIUM: int = 1
SAFETY_HIGH: int = 2

SITE_INCLUDE_INCLUDE: bool = True
SITE_INCLUDE_EXCLUDE: bool = False

FROM_DATE_DAY: str = 'day'
FROM_DATE_WEEK: str = 'week'
FROM_DATE_MONTH: str = 'month'
FROM_DATE_YEAR: str = 'year'


class GoogleSearchOrigin:
    ####################################################################################################################
    #
    # Const Google Search Origin variables
    #

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

    def __init__(self, search_type: str = 'search', base_url: str = 'www.google.com', ssl_certificate: bool = True,
    search: str = None, c2coff: bool = None, country: str = None, no_duplicate: bool = None,
    user_interface_language: str = None, and_operator: str = None, written_document_language: str = None,
    result_number: int = None, restrict_country: str = None, safety: int = None,
    start_page: int = None, site: str = None, site_include: bool = None, include_word: str = None,
    exclude_word: str = None, url_link: str = None, inclusive_search_range_start: int = None,
    inclusive_search_range_end: int = None, or_operator: str = None, additional_term: str = None,
    from_date: dict = None, related_url: str = None, client: str = None, search_engine_code: str = None,
    boost_country_search: str = None, character_encoding_scheme_interpreter: str = None,
    character_encoding_scheme_decoder: str = None, output_format: str = None, sort: str = None,
    idn_encoded_url: bool = None, picture_format: str = None, picture_size: str = None, picture_type: str = None,
    picture_color_filter: str = None, picture_color: str = None, picture_right: str = None):
        self.configuration = {}

        self.url: str = None
        self.base_url: str = None
        self.search_type: str = None
        self.protocol: str = None
        self.url_parameters: dict = {}

        self.import_configuration(self.__path_escaping_character__)

        self.parameter_url_base_url(base_url)
        self.parameter_search_type(search_type)
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

        self.assemble_url()

    def import_configuration(self, path: str) -> None:
        self.configuration.update(google_serach_yaml.Yaml().read_yaml(path))

    ####################################################################################################################
    #
    # Setup parameters
    #

    def parameter_url_base_url(self, base_url):
        if (base_url):
            self.base_url = base_url
        else:
            self.base_url = 'www.google.com'

    def parameter_search_type(self, search_type):
        if (search_type):
            self.search_type = search_type
        else:
            self.search_type = 'search'

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
            if (FROM_DATE_DAY in from_date and from_date[FROM_DATE_DAY] and from_date[FROM_DATE_DAY] >= 0):
                self.url_parameters['as_qdr'] = f'd{from_date[FROM_DATE_DAY]}'
            elif (FROM_DATE_WEEK in from_date and from_date[FROM_DATE_WEEK] and from_date[FROM_DATE_WEEK] >= 0):
                self.url_parameters['as_qdr'] = f'w{from_date[FROM_DATE_WEEK]}'
            elif (FROM_DATE_MONTH in from_date and from_date[FROM_DATE_MONTH] and from_date[FROM_DATE_MONTH] >= 0):
                self.url_parameters['as_qdr'] = f'm{from_date[FROM_DATE_MONTH]}'
            elif (FROM_DATE_YEAR in from_date and from_date[FROM_DATE_YEAR] and from_date[FROM_DATE_YEAR] >= 0):
                self.url_parameters['as_qdr'] = f'y{from_date[FROM_DATE_YEAR]}'

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

    ####################################################################################################################
    #
    # Assemble
    #

    def assemble_url(self) -> None:
        self.url = self.base_url
        if (self.protocol != None):
            self.url = '{protocol}://{url}'.format(protocol=self.protocol, url=self.url)
        if (self.url_parameters != {}):
            self.url = '{url_prefix}/{search_type}?{url_parameters}'.format(url_prefix=self.url,
            search_type=self.search_type, url_parameters=self.encode_url(self.url_parameters))

    def encode_url(self, parameters: dict) -> str:
        encoded_url = ''
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