import unittest
import src.google_search_origin as google_search_origin

class GoogleSearchOriginTest(unittest.TestCase):
    def test_no_param_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin().get_url(), 'https://www.google.com')
    
    ####################################################################################################################

    def test_enable_ssl_certificate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(ssl_certificate=True).get_url(),
        'https://www.google.com')

    def test_disable_ssl_certificate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(ssl_certificate=False).get_url(),
        'http://www.google.com')

    def test_none_ssl_certificate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(ssl_certificate=None).get_url(), 'www.google.com')

    ####################################################################################################################

    def test_simple_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search='sun').get_url(),
        'https://www.google.com/search?q=sun')
    
    def test_medium1_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search='sun beach').get_url(),
        'https://www.google.com/search?q=sun%20beach')
    
    def test_medium2_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search='I\'m here').get_url(),
        'https://www.google.com/search?q=I%27m%20here')

    def test_medium3_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search='I\'m "here"').get_url(),
        'https://www.google.com/search?q=I%27m%20%22here%22')
    
    def test_empty_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search='').get_url(),
        'https://www.google.com/search?q=')

    def test_none_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search=None).get_url(),
        'https://www.google.com')
    
    ####################################################################################################################

    def test_enable_c2coff_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(c2coff=True).get_url(),
        'https://www.google.com/search?c2coff=2')
    
    def test_disable_c2coff_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(c2coff=False).get_url(),
        'https://www.google.com/search?c2coff=1')

    def test_none_c2coff_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(c2coff=None).get_url(),
        'https://www.google.com')
    
    ####################################################################################################################

    def test_simple1_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='countryFR').get_url(),
        'https://www.google.com/search?cr=countryFR')
    
    def test_simple2_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='countryNZ').get_url(),
        'https://www.google.com/search?cr=countryNZ')

    def test_medium1_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='COUNTRYNZ').get_url(),
        'https://www.google.com/search?cr=countryNZ')

    def test_medium2_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='countrynz').get_url(),
        'https://www.google.com/search?cr=countryNZ')
    
    def test_medium3_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='COUNTRYnz').get_url(),
        'https://www.google.com/search?cr=countryNZ')
    
    def test_medium4_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='nz').get_url(),
        'https://www.google.com/search?cr=countryNZ')
    
    def test_medium5_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='NZ').get_url(),
        'https://www.google.com/search?cr=countryNZ')
    
    def test_unknown_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='unknown').get_url(),
        'https://www.google.com')

    def test_none_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_enable_no_duplicate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(no_duplicate=True).get_url(),
        'https://www.google.com/search?filter=0')
    
    def test_disable_no_duplicate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(no_duplicate=False).get_url(),
        'https://www.google.com/search?filter=1')
    
    def test_none_no_duplicate_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(no_duplicate=None).get_url(),
        'https://www.google.com')
    
    ####################################################################################################################

    def test_simple1_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='fr').get_url(),
        'https://www.google.com/search?hl=fr')
    
    def test_simple2_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='pt-PT').get_url(),
        'https://www.google.com/search?hl=pt-PT')
    
    def test_medium1_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='PT-PT').get_url(),
        'https://www.google.com/search?hl=pt-PT')
    
    def test_medium2_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='PT-pt').get_url(),
        'https://www.google.com/search?hl=pt-PT')

    def test_medium3_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='pt-pt').get_url(),
        'https://www.google.com/search?hl=pt-PT')
    
    def test_unknown_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='unknown').get_url(),
        'https://www.google.com')
    
    def test_none_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language=None).get_url(),
        'https://www.google.com')
    
    ####################################################################################################################

    def test_simple_and_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(and_operator='sun').get_url(),
        'https://www.google.com/search?hq=sun')
    
    def test_medium_and_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(and_operator='sun beach').get_url(),
        'https://www.google.com/search?hq=sun%20beach')
    
    def test_none_and_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(and_operator=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='lang_cs').get_url(),
        'https://www.google.com/search?lr=lang_cs')
    
    def test_simple2_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='lang_zh-TW').get_url(),
        'https://www.google.com/search?lr=lang_zh-TW')

    def test_medium1_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='LANG_CS').get_url(),
        'https://www.google.com/search?lr=lang_cs')

    def test_medium2_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='lang_zh-tw').get_url(),
        'https://www.google.com/search?lr=lang_zh-TW')
    
    def test_medium3_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='LANG_ZH-TW').get_url(),
        'https://www.google.com/search?lr=lang_zh-TW')
    
    def test_medium4_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='LANG_ZH-tw').get_url(),
        'https://www.google.com/search?lr=lang_zh-TW')
    
    def test_unknown_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='unknown').get_url(),
        'https://www.google.com')

    def test_none_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_result_number_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(result_number=10).get_url(),
        'https://www.google.com/search?num=10')
    
    def test_simple2_result_number_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(result_number=0).get_url(),
        'https://www.google.com')
    
    def test_simple3_result_number_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(result_number=-10).get_url(),
        'https://www.google.com')
    
    def test_none_result_number_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(result_number=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='countryFR').get_url(),
        'https://www.google.com/search?restrict=countryFR')
    
    def test_simple2_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='countryNZ').get_url(),
        'https://www.google.com/search?restrict=countryNZ')

    def test_medium1_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='COUNTRYNZ').get_url(),
        'https://www.google.com/search?restrict=countryNZ')

    def test_medium2_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='countrynz').get_url(),
        'https://www.google.com/search?restrict=countryNZ')
    
    def test_medium3_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='COUNTRYnz').get_url(),
        'https://www.google.com/search?restrict=countryNZ')
    
    def test_medium4_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='nz').get_url(),
        'https://www.google.com/search?restrict=countryNZ')
    
    def test_medium5_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='NZ').get_url(),
        'https://www.google.com/search?restrict=countryNZ')
    
    def test_unknown_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='unknown').get_url(),
        'https://www.google.com')

    def test_none_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_safety_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(safety=0).get_url(),
        'https://www.google.com/search?safe=off')
    
    def test_simple2_safety_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(safety=1).get_url(),
        'https://www.google.com/search?safe=medium')
    
    def test_simple3_safety_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(safety=2).get_url(),
        'https://www.google.com/search?safe=high')
    
    def test_simple4_safety_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(safety=3).get_url(),
        'https://www.google.com')

    def test_none_safety_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(safety=None).get_url(),
        'https://www.google.com')
    
    ####################################################################################################################
    
    def test_simple1_start_page_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(start_page=10).get_url(),
        'https://www.google.com/search?start=10')
    
    def test_simple2_start_page_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(start_page=0).get_url(),
        'https://www.google.com')

    def test_simple3_start_page_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(start_page=-10).get_url(),
        'https://www.google.com')

    def test_none_start_page_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(start_page=None).get_url(),
        'https://www.google.com')

if (__name__ == '__main__'):
    unittest.main()