from typing import List
import requests
import src.common.yaml as google_serach_yaml

class GoogleSearchOrigin:
    ####################################################################################################################
    #
    # Const variables
    #

    __country_collection_values__: str = 'country_collection_values'
    __supported_interface_languages__: str = 'supported_interface_languages'
    __language_collection_values__: str = 'language_collection_values'

    SAFETY_OFF: int = 0
    SAFETY_MEDIUM: int = 1
    SAFETY_HIGH: int = 2

    ####################################################################################################################
    #
    # Initialisation
    #

    def __init__(self, ssl_certificate: bool = True, search: str = None, c2coff: bool = None, country: str = None,
    no_duplicate: bool = None, user_interface_language: str = None, and_operator: str = None,
    written_document_language: str = None, result_number: int = None, restrict_country: str = None, safety: int = None,
    start_page: int = None, site: str = None, inclusion: bool = None, and_include_words: str = None,
    exclusion_term: str = None, url_result: str = None):
        self.import_configuration()

        self.url = 'www.google.com'
        self.protocol = None
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
        if (search != None):
            self.url_parameters['q'] = f'q={search}'


    def parameter_c2coff(self, c2coff: bool) -> None:
        if (c2coff != None):
            if (c2coff):
                self.url_parameters['c2coff'] = 'c2coff=2'
            else:
                self.url_parameters['c2coff'] = 'c2coff=1'


    def parameter_country(self, argument: str, country: str) -> None:
        if (country != None):
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
        if (user_interface_language != None):
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
        if (and_operator != None):
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

    def parameter_start_page(self, start_page) -> None:
        if (start_page != None and start_page > 0):
            self.url_parameters['start'] = f'start={start_page}'

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