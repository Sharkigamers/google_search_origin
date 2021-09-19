from typing import List
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

    __country_collection_values__: str = 'country_collection_values'
    __supported_interface_languages__: str = 'supported_interface_languages'
    __language_collection_values__: str = 'language_collection_values'

    ####################################################################################################################
    #
    # Initialisation
    #

    def __init__(self, ssl_certificate: bool = True, search: str = None, c2coff: bool = None, country: str = None,
    no_duplicate: bool = None, user_interface_language: str = None, and_operator: str = None,
    written_document_language: str = None, result_number: int = None, restrict_country: str = None, safety: int = None,
    start_page: int = None, site: str = None, site_include: bool = None, include_word: str = None,
    exclude_word: str = None, url_link: str = None, inclusive_search_range_start: int = None,
    inclusive_search_range_end: int = None, or_operator: str = None, additional_term: str = None,
    from_date: dict = None, related_url: str = None):
        self.import_configuration()

        self.url: str = 'www.google.com'
        self.protocol: str = None
        self.url_parameters: dict = {}

        self.parameter_ssl_certificate(ssl_certificate)
        self.parameter_search(search)
        self.parameter_c2coff(c2coff)
        self.parameter_country('cr', country)
        self.parameter_no_duplicate(no_duplicate)
        self.parameter_user_interface_language(user_interface_language)
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

        self.assemble_url()

    def import_configuration(self):
        self.configuration = google_serach_yaml.Yaml().read_yaml('src/configuration/configuration.yaml')

    ####################################################################################################################
    #
    # Setup parameters
    #

    def parameter_ssl_certificate(self, ssl_certificate: bool) -> None:
        if (ssl_certificate != None):
            if (ssl_certificate):
                self.protocol = 'https'
            else:
                self.protocol = 'http'

    def parameter_search(self, search: str) -> None:
        if (search):
            self.url_parameters['q'] = f'q={search}'


    def parameter_c2coff(self, c2coff: bool) -> None:
        if (c2coff != None):
            if (c2coff):
                self.url_parameters['c2coff'] = 'c2coff=2'
            else:
                self.url_parameters['c2coff'] = 'c2coff=1'


    def parameter_country(self, argument: str, country: str) -> None:
        if (country):
            if (len(country) == 2):
                if (not country.isupper()):
                    country = f'country{country.upper()}'
                else:
                    country = f'country{country}'
            if (len(country) == 9):
                if (not country[:7].islower() or not country[7:].isupper()):
                    country = f'{country[:7].lower()}{country[7:].upper()}'
            if (country in self.configuration[self.__country_collection_values__]):
                self.url_parameters['cr'] = f'{argument}={country}'


    def parameter_no_duplicate(self, no_duplicate: bool) -> None:
        if (no_duplicate != None):
            if (no_duplicate):
                self.url_parameters['filter'] = f'filter=0'
            else:
                self.url_parameters['filter'] = f'filter=1'

    def parameter_user_interface_language(self, user_interface_language: str) -> None:
        if (user_interface_language):
            if (len(user_interface_language) == 2):
                if (not user_interface_language.islower()):
                    user_interface_language = user_interface_language.lower()
            else:
                splited_user_interface_language = user_interface_language.split('-')
                if (len(splited_user_interface_language) == 2):
                    if (not splited_user_interface_language[0].islower() or
                    not splited_user_interface_language[1].isupper()):
                        user_interface_language = (f'{splited_user_interface_language[0].lower()}-'
                        f'{splited_user_interface_language[1].upper()}')
                else:
                    return
            if (user_interface_language in self.configuration[self.__supported_interface_languages__]):
                self.url_parameters['hl'] = f'hl={user_interface_language}'

    def parameter_and_operator(self, and_operator: str):
        if (and_operator):
            self.url_parameters['hq'] = f'hq={and_operator}'

    def parameter_written_document_language(self, written_document_language: str) -> None:
        if (written_document_language):
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
            if (written_document_language in self.configuration[self.__language_collection_values__]):
                self.url_parameters['lr'] = f'lr={written_document_language}'

    def parameter_result_number(self, result_number: int) -> None:
        if (result_number != None and result_number > 0):
            self.url_parameters['num'] = f'num={result_number}'

    def parameter_safety(self, safety: int) -> None:
        if (safety != None):
            if (safety == 0):
                self.url_parameters['safe'] = 'safe=off'
            elif (safety == 1):
                self.url_parameters['safe'] = 'safe=medium'
            elif (safety == 2):
                self.url_parameters['safe'] = 'safe=high'

    def parameter_start_page(self, start_page: int) -> None:
        if (start_page != None and start_page > 0):
            self.url_parameters['start'] = f'start={start_page}'

    def parameter_site(self, site: str) -> None:
        if (site):
            self.url_parameters['site'] = f'as_sitesearch={site}'
    
    def parameter_site_include(self, site_include: bool) -> None:
        if (site_include != None):
            if (site_include):
                self.url_parameters['site_include'] = 'as_dt=i'
            else:
                self.url_parameters['site_include'] = 'as_dt=e'
    
    def parameter_include_word(self, include_word: str) -> None:
        if (include_word):
            self.url_parameters['include_word'] = f'as_epq={include_word}'

    def parameter_exclude_word(self, exclude_word: str) -> None:
        if (exclude_word):
            self.url_parameters['exclude_word'] = f'as_eq={exclude_word}'

    def parameter_url_link(self, url_link: str) -> None:
        if (url_link):
            self.url_parameters['url_link'] = f'as_lq={url_link}'

    def parameter_inclusive_search_range_start(self, inclusive_search_range_start: int) -> None:
        if (inclusive_search_range_start != None and inclusive_search_range_start > 0):
            self.url_parameters['inclusive_search_range_start'] = f'as_nlo={inclusive_search_range_start}'
    
    def parameter_inclusive_search_range_end(self, inclusive_search_range_end: int) -> None:
        if (inclusive_search_range_end != None and inclusive_search_range_end > 0):
            self.url_parameters['inclusive_search_range_end'] = f'as_nhi={inclusive_search_range_end}'

    def parameter_or_operator(self, or_operator: str) -> None:
        if (or_operator):
            self.url_parameters['or_operator'] = f'as_oq={or_operator}'
    
    def parameter_additional_term(self, additional_term: str) -> None:
        if (additional_term):
            self.url_parameters['additional_term'] = f'as_q={additional_term}'

    def parameter_from_date(self, from_date: dict) -> None:
        if (from_date):
            if (FROM_DATE_DAY in from_date and from_date[FROM_DATE_DAY] and from_date[FROM_DATE_DAY] >= 0):
                self.url_parameters['from_date'] = f'as_qdr=d{from_date[FROM_DATE_DAY]}'
            elif (FROM_DATE_WEEK in from_date and from_date[FROM_DATE_WEEK] and from_date[FROM_DATE_WEEK] >= 0):
                self.url_parameters['from_date'] = f'as_qdr=w{from_date[FROM_DATE_WEEK]}'
            elif (FROM_DATE_MONTH in from_date and from_date[FROM_DATE_MONTH] and from_date[FROM_DATE_MONTH] >= 0):
                self.url_parameters['from_date'] = f'as_qdr=m{from_date[FROM_DATE_MONTH]}'
            elif (FROM_DATE_YEAR in from_date and from_date[FROM_DATE_YEAR] and from_date[FROM_DATE_YEAR] >= 0):
                self.url_parameters['from_date'] = f'as_qdr=y{from_date[FROM_DATE_YEAR]}'

    def parameter_related_url(self, related_url: str) -> None:
        if (related_url):
            self.url_parameters['related_url'] = f'as_rq={related_url}'

    ####################################################################################################################
    #
    # Assemble
    #

    def assemble_url(self) -> None:
        if (self.protocol != None):
            self.url = '{protocol}://{url}'.format(protocol=self.protocol, url=self.url)
        if (self.url_parameters != {}):
            self.url = '{url_prefix}/search?{url_parameters}'.format(url_prefix=self.url,
            url_parameters='&'.join(self.url_parameters.values()))
        self.url = self.url.replace(' ', '%20').replace('"', '%22').replace('\'', '%27')

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