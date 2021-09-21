import unittest
import src.google_search_origin as google_search_origin

class GoogleSearchOriginTest(unittest.TestCase):
    def test_no_param_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin().get_url(), 'https://www.google.com')
    
    ####################################################################################################################

    def test_simple1_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='imghp').get_url(),
        'https://www.google.com')

    def test_simple2_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='imghp', search='dog').get_url(),
        'https://www.google.com/imghp?q=dog')
    
    def test_empty1_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='imghp', search='').get_url(),
        'https://www.google.com')

    def test_empty2_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='').get_url(),
        'https://www.google.com')

    def test_none_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple_tbm_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(filter='isch').get_url(),
        'https://www.google.com/search?tbm=isch')
    
    def test_empty_tbm_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(filter='').get_url(),
        'https://www.google.com')

    def test_none_tbm_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(filter=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple_base_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(base_url='www.yahoo.com').get_url(),
        'https://www.yahoo.com')
    
    def test_empty_base_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(base_url='').get_url(),
        'https://www.google.com')

    def test_none_base_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(base_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='imghp', search='sun').get_url(),
        'https://www.google.com/imghp?q=sun')
    
    def test_empty_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type='', search='sun').get_url(),
        'https://www.google.com/search?q=sun')

    def test_none_search_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_type=None).get_url(),
        'https://www.google.com')

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
        'https://www.google.com')

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

    def test_empty_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(country='').get_url(),
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
    
    def test_empty_user_interface_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(user_interface_language='').get_url(),
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
    
    def test_empty_and_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(and_operator='').get_url(),
        'https://www.google.com')

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

    def test_empty_written_document_language_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(written_document_language='').get_url(),
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

    def test_empty_restrict_country_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(restrict_country='').get_url(),
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
    
    ####################################################################################################################

    def test_simple1_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site='www.google.com').get_url(),
        'https://www.google.com/search?as_sitesearch=www.google.com')
    
    def test_empty_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site='').get_url(),
        'https://www.google.com')

    def test_none_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_enable_site_include_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site='www.google.com', site_include=True).get_url(),
        'https://www.google.com/search?as_sitesearch=www.google.com&as_dt=i')
    
    def test_disable_site_include_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site='www.google.com', site_include=False).get_url(),
        'https://www.google.com/search?as_sitesearch=www.google.com&as_dt=e')

    def test_none_site_include_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(site='www.google.com', site_include=None).get_url(),
        'https://www.google.com/search?as_sitesearch=www.google.com')

    ####################################################################################################################

    def test_simple1_include_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(include_word='music').get_url(),
        'https://www.google.com/search?as_epq=music')
    
    def test_empty_include_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(include_word='').get_url(),
        'https://www.google.com')

    def test_none_include_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(include_word=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_exclude_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(exclude_word='music').get_url(),
        'https://www.google.com/search?as_eq=music')
    
    def test_empty_exclude_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(exclude_word='').get_url(),
        'https://www.google.com')

    def test_none_exclude_word_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(exclude_word=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_inclusive_search_range_start_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_start=10).get_url(),
        'https://www.google.com/search?as_nlo=10')
    
    def test_simple2_inclusive_search_range_start_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_start=0).get_url(),
        'https://www.google.com')

    def test_simple3_inclusive_search_range_start_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_start=-10).get_url(),
        'https://www.google.com')

    def test_none_inclusive_search_range_start_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_start=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_inclusive_search_range_end_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_end=20).get_url(),
        'https://www.google.com/search?as_nhi=20')
    
    def test_simple2_inclusive_search_range_end_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_end=0).get_url(),
        'https://www.google.com')

    def test_simple3_inclusive_search_range_end_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_end=-20).get_url(),
        'https://www.google.com')

    def test_none_inclusive_search_range_end_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(inclusive_search_range_end=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_or_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(or_operator='sheep').get_url(),
        'https://www.google.com/search?as_oq=sheep')

    def test_empty_or_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(or_operator='').get_url(),
        'https://www.google.com')

    def test_none_or_operator_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(or_operator=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_additional_term_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(additional_term='sheep').get_url(),
        'https://www.google.com/search?as_q=sheep')

    def test_empty_additional_term_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(additional_term='').get_url(),
        'https://www.google.com')

    def test_none_additional_term_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(additional_term=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_day_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'day': 10}).get_url(),
        'https://www.google.com/search?as_qdr=d10')
    
    def test_week_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'week': 10}).get_url(),
        'https://www.google.com/search?as_qdr=w10')
    
    def test_month_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'month': 10}).get_url(),
        'https://www.google.com/search?as_qdr=m10')
    
    def test_year_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'year': 10}).get_url(),
        'https://www.google.com/search?as_qdr=y10')

    def test_none_day_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'day': None}).get_url(),
        'https://www.google.com')
    
    def test_none_week_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'week': None}).get_url(),
        'https://www.google.com')
    
    def test_none_month_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'month': None}).get_url(),
        'https://www.google.com')
    
    def test_none_year_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={'year': None}).get_url(),
        'https://www.google.com')

    def test_empty_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date={}).get_url(),
        'https://www.google.com')

    def test_none_from_date_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(from_date=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_related_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(related_url='www.github.com').get_url(),
        'https://www.google.com/search?as_rq=www%2Egithub%2Ecom')

    def test_empty_related_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(related_url='').get_url(),
        'https://www.google.com')

    def test_none_related_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(related_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_client_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(client='google-csbe').get_url(),
        'https://www.google.com/search?client=google-csbe')

    def test_empty_client_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(client='').get_url(),
        'https://www.google.com')

    def test_none_client_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(client=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_search_engine_code_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_engine_code='00255077836266642015:u-scht7a-8i')
        .get_url(), 'https://www.google.com/search?cx=00255077836266642015:u-scht7a-8i')

    def test_empty_search_engine_code_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_engine_code='').get_url(),
        'https://www.google.com')

    def test_none_search_engine_code_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(search_engine_code=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_boost_country_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(boost_country_search='fr').get_url(),
        'https://www.google.com/search?gl=fr')
    
    def test_simple2_boost_country_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(boost_country_search='FR').get_url(),
        'https://www.google.com/search?gl=fr')
    
    def test_unknown_boost_country_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(boost_country_search='unknown').get_url(),
        'https://www.google.com')
    
    def test_empty_boost_country_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(boost_country_search='').get_url(),
        'https://www.google.com')

    def test_none_boost_country_search_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(boost_country_search=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_character_encoding_scheme_interpreter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_interpreter='utf8')
        .get_url(), 'https://www.google.com/search?ie=utf8')

    def test_empty_character_encoding_scheme_interpreter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_interpreter='').get_url(),
        'https://www.google.com')

    def test_none_character_encoding_scheme_interpreter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_interpreter=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_character_encoding_scheme_decoder_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_decoder='utf8')
        .get_url(), 'https://www.google.com/search?oe=utf8')

    def test_empty_character_encoding_scheme_decoder_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_decoder='').get_url(),
        'https://www.google.com')

    def test_none_character_encoding_scheme_decoder_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(character_encoding_scheme_decoder=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_output_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(output_format='xml_no_dtd')
        .get_url(), 'https://www.google.com/search?output=xml_no_dtd')
    
    def test_simple1_output_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(output_format='xml')
        .get_url(), 'https://www.google.com/search?output=xml')

    def test_empty_output_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(output_format='').get_url(),
        'https://www.google.com')

    def test_none_output_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(output_format=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_sort_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(sort='beach')
        .get_url(), 'https://www.google.com/search?sort=beach')

    def test_empty_sort_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(sort='').get_url(),
        'https://www.google.com')

    def test_none_sort_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(sort=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_enable_idn_encoded_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(idn_encoded_url=True).get_url(),
        'https://www.google.com/search?ud=1')
    
    def test_disable_idn_encoded_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(idn_encoded_url=False).get_url(),
        'https://www.google.com/search?ud=0')
    
    def test_none_idn_encoded_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(idn_encoded_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_format='bmp')
        .get_url(), 'https://www.google.com/search?as_filetype=bmp')
    
    def test_medium1_picture_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_format='BMP')
        .get_url(), 'https://www.google.com/search?as_filetype=bmp')

    def test_empty_picture_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_format='').get_url(),
        'https://www.google.com')

    def test_none_picture_format_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_format=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_size_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_size='icon')
        .get_url(), 'https://www.google.com/search?imgsz=icon')
    
    def test_medium1_picture_size_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_size='ICON')
        .get_url(), 'https://www.google.com/search?imgsz=icon')

    def test_empty_picture_size_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_size='').get_url(),
        'https://www.google.com')

    def test_none_picture_size_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_size=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_type='face')
        .get_url(), 'https://www.google.com/search?imgtype=face')
    
    def test_medium1_picture_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_type='FACE')
        .get_url(), 'https://www.google.com/search?imgtype=face')

    def test_empty_picture_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_type='').get_url(),
        'https://www.google.com')

    def test_none_picture_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_type=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_color_filter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color_filter='mono')
        .get_url(), 'https://www.google.com/search?imgc=mono')
    
    def test_medium1_picture_color_filter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color_filter='MONO')
        .get_url(), 'https://www.google.com/search?imgc=mono')

    def test_empty_picture_color_filter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color_filter='').get_url(),
        'https://www.google.com')

    def test_none_picture_color_filter_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color_filter=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_color_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color='yellow')
        .get_url(), 'https://www.google.com/search?imgcolor=yellow')
    
    def test_medium1_picture_color_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color='YELLOW')
        .get_url(), 'https://www.google.com/search?imgcolor=yellow')

    def test_empty_picture_color_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color='').get_url(),
        'https://www.google.com')

    def test_none_picture_color_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_color=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_picture_right_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_right='cc_attribute')
        .get_url(), 'https://www.google.com/search?as_rights=cc_attribute')
    
    def test_medium1_picture_right_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_right='CC_ATTRIBUTE')
        .get_url(), 'https://www.google.com/search?as_rights=cc_attribute')

    def test_empty_picture_right_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_right='').get_url(),
        'https://www.google.com')

    def test_none_picture_right_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(picture_right=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_links=['www.google.com'])
        .get_url(), 'https://www.google.com/search?q=link%3Awww%2Egoogle%2Ecom')
    
    def test_medium1_dorks_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_links=['www.google.com', 'www.yahoo.com'])
        .get_url(), 'https://www.google.com/search?q=link%3Awww%2Egoogle%2Ecom%20link%3Awww%2Eyahoo%2Ecom')

    def test_empty_dorks_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_links='').get_url(),
        'https://www.google.com')

    def test_none_dorks_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_links=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_or_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_or=['drum'])
        .get_url(), 'https://www.google.com/search?q=drum')
    
    def test_medium1_dorks_or_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_or=['drum', 'music'])
        .get_url(), 'https://www.google.com/search?q=drum%20OR%20music')

    def test_empty_dorks_or_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_or='').get_url(),
        'https://www.google.com')

    def test_none_dorks_or_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_or=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_theme_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_theme_exclusion=['bass'])
        .get_url(), 'https://www.google.com/search?q=%2Dbass')
    
    def test_medium1_dorks_theme_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_theme_exclusion=['bass', 'drum'])
        .get_url(), 'https://www.google.com/search?q=%2Dbass%20%2Ddrum')

    def test_empty_dorks_theme_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_theme_exclusion='').get_url(),
        'https://www.google.com')

    def test_none_dorks_theme_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_theme_exclusion=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_file_type_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type_exclusion=['PDF'])
        .get_url(), 'https://www.google.com/search?q=%2Dfiletype%3APDF')
    
    def test_medium1_dorks_file_type_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type_exclusion=['PDF', 'DOC'])
        .get_url(), 'https://www.google.com/search?q=%2Dfiletype%3APDF%20%2Dfiletype%3ADOC')

    def test_empty_dorks_file_type_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type_exclusion='').get_url(),
        'https://www.google.com')

    def test_none_dorks_file_type_exclusion_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type_exclusion=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_file_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type=['PDF'])
        .get_url(), 'https://www.google.com/search?q=filetype%3APDF')
    
    def test_medium1_dorks_file_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type=['PDF', 'DOC'])
        .get_url(), 'https://www.google.com/search?q=filetype%3APDF%20filetype%3ADOC')

    def test_empty_dorks_file_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type='').get_url(),
        'https://www.google.com')

    def test_none_dorks_file_type_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_file_type=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_and_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_and=['drum'])
        .get_url(), 'https://www.google.com/search?q=drum')
    
    def test_medium1_dorks_and_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_and=['drum', 'bass'])
        .get_url(), 'https://www.google.com/search?q=drum%2Bbass')

    def test_empty_dorks_and_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_and='').get_url(),
        'https://www.google.com')

    def test_none_dorks_and_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_and=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_words_in_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_links=['pdf'])
        .get_url(), 'https://www.google.com/search?q=allinlinks%3Apdf')
    
    def test_medium1_dorks_words_in_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_links=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=allinlinks%3Apdf%20allinlinks%3Adoc')

    def test_empty_dorks_words_in_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_links='').get_url(),
        'https://www.google.com')

    def test_none_dorks_words_in_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_links=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_should_appear_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_should_appear=['pdf'])
        .get_url(), 'https://www.google.com/search?q=%22pdf%22')
    
    def test_medium1_dorks_should_appear_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_should_appear=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=%22pdf%22%20%22doc%22')

    def test_empty_dorks_should_appear_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_should_appear='').get_url(),
        'https://www.google.com')

    def test_none_dorks_should_appear_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_should_appear=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_related_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_related_links=['www.google.com'])
        .get_url(), 'https://www.google.com/search?q=related%3Awww%2Egoogle%2Ecom')
    
    def test_medium1_dorks_related_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(
        dorks_related_links=['www.google.com', 'www.yahoo.com'])
        .get_url(), 'https://www.google.com/search?q=related%3Awww%2Egoogle%2Ecom%20related%3Awww%2Eyahoo%2Ecom')

    def test_empty_dorks_related_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_related_links='').get_url(),
        'https://www.google.com')

    def test_none_dorks_related_links_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_related_links=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_words_in_text_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_text=['pdf'])
        .get_url(), 'https://www.google.com/search?q=allintext%3Apdf')
    
    def test_medium1_dorks_words_in_text_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_text=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=allintext%3Apdf%20allintext%3Adoc')

    def test_empty_dorks_words_in_text_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_text='').get_url(),
        'https://www.google.com')

    def test_none_dorks_words_in_text_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_text=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_word_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_title=['pdf'])
        .get_url(), 'https://www.google.com/search?q=intitle%3Apdf')
    
    def test_medium1_dorks_word_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_title=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=intitle%3Apdf%20intitle%3Adoc')

    def test_empty_dorks_word_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_title='').get_url(),
        'https://www.google.com')

    def test_none_dorks_word_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_title=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_words_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_title=['pdf'])
        .get_url(), 'https://www.google.com/search?q=allintitle%3Apdf')
    
    def test_medium1_dorks_words_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_title=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=allintitle%3Apdf%20allintitle%3Adoc')

    def test_empty_dorks_words_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_title='').get_url(),
        'https://www.google.com')

    def test_none_dorks_words_in_title_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_title=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_word_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_url=['pdf'])
        .get_url(), 'https://www.google.com/search?q=inurl%3Apdf')
    
    def test_medium1_dorks_word_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_url=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=inurl%3Apdf%20inurl%3Adoc')

    def test_empty_dorks_word_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_url='').get_url(),
        'https://www.google.com')

    def test_none_dorks_word_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_word_in_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=['pdf'])
        .get_url(), 'https://www.google.com/search?q=allinurl%3Apdf')
    
    def test_medium1_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=allinurl%3Apdf%20allinurl%3Adoc')

    def test_empty_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url='').get_url(),
        'https://www.google.com')

    def test_none_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=['pdf'])
        .get_url(), 'https://www.google.com/search?q=allinurl%3Apdf')
    
    def test_medium1_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=['pdf', 'doc'])
        .get_url(), 'https://www.google.com/search?q=allinurl%3Apdf%20allinurl%3Adoc')

    def test_empty_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url='').get_url(),
        'https://www.google.com')

    def test_none_dorks_words_in_url_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_words_in_url=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_info_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_info=['www.google.com'])
        .get_url(), 'https://www.google.com/search?q=info%3Awww%2Egoogle%2Ecom')
    
    def test_medium1_dorks_info_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_info=['www.google.com', 'www.yahoo.com'])
        .get_url(), 'https://www.google.com/search?q=info%3Awww%2Egoogle%2Ecom%20info%3Awww%2Eyahoo%2Ecom')

    def test_empty_dorks_info_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_info='').get_url(),
        'https://www.google.com')

    def test_none_dorks_info_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_info=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_cache_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_cache=['securitytrails.com'])
        .get_url(), 'https://www.google.com/search?q=cache%3Asecuritytrails%2Ecom')
    
    def test_medium1_dorks_cache_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(
        dorks_cache=['securitytrails.com', 'google.com'])
        .get_url(), 'https://www.google.com/search?q=cache%3Asecuritytrails%2Ecom%20cache%3Agoogle%2Ecom')

    def test_empty_dorks_cache_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_cache='').get_url(),
        'https://www.google.com')

    def test_none_dorks_cache_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_cache=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_anchor_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_anchor=['cyber'])
        .get_url(), 'https://www.google.com/search?q=inanchor%3Acyber')
    
    def test_medium1_dorks_anchor_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_anchor=['cyber', 'security'])
        .get_url(), 'https://www.google.com/search?q=inanchor%3Acyber%20inanchor%3Asecurity')

    def test_empty_dorks_anchor_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_anchor='').get_url(),
        'https://www.google.com')

    def test_none_dorks_anchor_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_anchor=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_define_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_define=['cyber'])
        .get_url(), 'https://www.google.com/search?q=define%3Acyber')
    
    def test_medium1_dorks_define_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_define=['cyber', 'security'])
        .get_url(), 'https://www.google.com/search?q=define%3Acyber%20define%3Asecurity')

    def test_empty_dorks_define_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_define='').get_url(),
        'https://www.google.com')

    def test_none_dorks_define_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_define=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_stocks_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_stocks=['cyber'])
        .get_url(), 'https://www.google.com/search?q=stocks%3Acyber')
    
    def test_medium1_dorks_stocks_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_stocks=['cyber', 'security'])
        .get_url(), 'https://www.google.com/search?q=stocks%3Acyber%20stocks%3Asecurity')

    def test_empty_dorks_stocks_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_stocks='').get_url(),
        'https://www.google.com')

    def test_none_dorks_stocks_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_stocks=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_phonebook_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_phonebook=['101111111111'])
        .get_url(), 'https://www.google.com/search?q=phonebook%3A101111111111')
    
    def test_medium1_dorks_phonebook_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_phonebook=['101111111111', '066666666666'])
        .get_url(), 'https://www.google.com/search?q=phonebook%3A101111111111%20phonebook%3A066666666666')

    def test_empty_dorks_phonebook_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_phonebook='').get_url(),
        'https://www.google.com')

    def test_none_dorks_phonebook_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_phonebook=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_maps_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_maps=['London'])
        .get_url(), 'https://www.google.com/search?q=maps%3ALondon')
    
    def test_medium1_dorks_maps_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_maps=['London', 'Madrid'])
        .get_url(), 'https://www.google.com/search?q=maps%3ALondon%20maps%3AMadrid')

    def test_empty_dorks_maps_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_maps='').get_url(),
        'https://www.google.com')

    def test_none_dorks_maps_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_maps=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_book_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_book=['MyHeroAcademia'])
        .get_url(), 'https://www.google.com/search?q=book%3AMyHeroAcademia')
    
    def test_medium1_dorks_book_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_book=['MyHeroAcademia', 'Deku'])
        .get_url(), 'https://www.google.com/search?q=book%3AMyHeroAcademia%20book%3ADeku')

    def test_empty_dorks_book_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_book='').get_url(),
        'https://www.google.com')

    def test_none_dorks_book_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_book=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_movie_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_movie=['StarWars'])
        .get_url(), 'https://www.google.com/search?q=movie%3AStarWars')
    
    def test_medium1_dorks_movie_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_movie=['StarWars', 'KingKong'])
        .get_url(), 'https://www.google.com/search?q=movie%3AStarWars%20movie%3AKingKong')

    def test_empty_dorks_movie_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_movie='').get_url(),
        'https://www.google.com')

    def test_none_dorks_movie_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_movie=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

    def test_simple1_dorks_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_site=['www.github.com'])
        .get_url(), 'https://www.google.com/search?q=site%3Awww%2Egithub%2Ecom')
    
    def test_medium1_dorks_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_site=['www.github.com', 'www.google.com'])
        .get_url(), 'https://www.google.com/search?q=site%3Awww%2Egithub%2Ecom%20site%3Awww%2Egoogle%2Ecom')

    def test_empty_dorks_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_site='').get_url(),
        'https://www.google.com')

    def test_none_dorks_site_url(self):
        self.assertEqual(google_search_origin.GoogleSearchOrigin(dorks_site=None).get_url(),
        'https://www.google.com')

    ####################################################################################################################

if (__name__ == '__main__'):
    unittest.main()