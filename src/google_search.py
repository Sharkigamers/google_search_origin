import requests
import src.common.yaml as google_serach_yaml

class GoogleSearch:
    __country_collection_values__: str = 'country_collection_values'
    __supported_interface_languages__: str = 'supported_interface_languages'
    __language_collection_values__: str = 'language_collection_values'

    def __init__(self, search: str = '', c2coff: bool = True, country: str = None, no_duplicate: bool = False,
    user_interface_language: str = None, and_operator: str = None, written_document_language: str = None,
    result_number: int = 10, restriction: str = None, safety: int = 0, start: int = 0, site: str = 'www.google.com',
    inclusion: bool = True, and_include_words: str = None, exclusion_term: str = None, url_result: str = None):
        self.import_configuration()
        self.url_parameters: list = [str]

    def import_configuration(self):
        self.configuration = google_serach_yaml.Yaml().read_yaml('src/configuration/configuration.yaml')

    def parameter_search(self, search: str) -> None:
        if (search != None):
            self.url_parameters.append(f'q={search}')
    
    def parameter_c2coff(self, c2coff: bool) -> None:
        if (c2coff != None):
            if (c2coff):
                self.url_parameters.append('c2coff=2')
            else:
                self.url_parameters.append(f'c2coff=1')
    
    def parameter_country(self, country: str) -> None:
        if (country != None):
            if (len(country) == 2):
                if (not country.islower()):
                    country = f'country{country}'
                if (not country.isupper()):
                    country = f'country{country.upper()}'
            if (len(country) == 9):
                if (not country[:7].islower or not country[7:].isupper):
                    country = f'country{country[7:].isupper}'
                if (country in self.configuration[self.__country_collection_values__]):
                    self.url_parameters.append(country)
    
    def parameter_no_duplicate(self, no_duplicate: bool) -> None:
        if (no_duplicate != None):
            if (no_duplicate):
                self.url_parameters.append(f'filter=0')
            else:
                self.url_parameters.append(f'filter=1')

    def parameter_user_interface_language(self, user_interface_language: str) -> None:
        if (user_interface_language != None):
            if (len(user_interface_language) == 2):
                if (not user_interface_language.islower()):
                    user_interface_language = user_interface_language.lower()
            else:
                slited_user_interface_language = user_interface_language.split('-')
                if (len(slited_user_interface_language) == 2):
                    if (not slited_user_interface_language[0].islower() or
                    not slited_user_interface_language[1].isupper()):
                        user_interface_language = f'{slited_user_interface_language[0].lower()}'
                        f'-{slited_user_interface_language[1].upper()}'
                else:
                    return
            if (user_interface_language in self.configuration[self.__supported_interface_languages__]):
                self.url_parameters.append(user_interface_language)

    def parameter_and_operator(self, and_operator: str):
        if (and_operator != None):
            self.url_parameters.append(f'hq={and_operator}')

    def parameter_written_document_language(self, written_document_language: str) -> None:
        if (written_document_language):
            if (len(written_document_language) == 7):
                if (not written_document_language.islower()):
                    written_document_language = written_document_language.lower()
            else:
                slited_written_document_language = written_document_language.split('-')
                if (len(slited_written_document_language) == 2):
                    if (not slited_written_document_language[0].islower() or
                    not slited_written_document_language[1].isupper()):
                        written_document_language = f'{slited_written_document_language[0].lower()}'
                        f'-{slited_written_document_language[1].upper()}'
                else:
                    return
            if (written_document_language in self.configuration[self.__language_collection_values__]):
                self.url_parameters.append(written_document_language)


    def clear_url_parameters(self) -> None:
        self.url_parameters = [str]