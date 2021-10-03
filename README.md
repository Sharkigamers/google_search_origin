# Google Search Origin

Google Search Origin is a library for searching via requests (like on Google) and formating urls via parameters.

Google Search Origin uses `requests` and `BeautifulSoup4`.

Its main functionnality is used to scrap google.

It can do so much more thanks to the various parameters available on it.

## Installation

To install, run the following command:

`python3 -m pip install google-search-origin`

or

`pip3 install google-search-origin`

## Usage

To get results for a search.

- You have to initialize the class `GoogleSearchOrigin` with the parameters you want to use.
- You have to request the url with the method `request_url`.
- You can collect the output using, for example `get_all_links` if you only want links.

After that you can modify and remove the parameters with the methods of your need.

When you're modifying the parameters you have assemble the url with the method `assemble_url`.

```
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
```

## Parameters

Google Search Origin has a lot of parameters. Here the list explained below :

- search_type (str): The type of the search (imghp, search, ...)
- filter (str): The categroy of the search:
  - 'app'
  - 'blg'
  - 'bks'
  - 'dsc'
  - 'isch'
  - 'nws'
  - 'pts'
  - 'plcs'
  - 'rcp'
  - 'shop'
  - 'vid'
- base_url (str): The base of the url (www.google.com)
- ssl_certificate (bool): True for https / False for http
- search (str): A basic search
- c2coff (bool): True to enable / False to disable the Simplified and Traditional Chinese Search
- country (str): Restrict the search to documents originating in a particular country (countryFR, countryNZ, ...)
- no_duplicate (bool): True to enable / False to disable the duplicate content
- user_interface_language (str): Specify the language interface (pt-PT, fr, ...)
- and_operator (str): Add terms to your search
- written_document_language (str): Restrict search results to document written in a specific language (lang_cs, lang_zh-TW, ...)
- result_number (int): Return the number of results
- restrict_country (str): Limit result to national specific pages (countryFR, countryNZ, ...)
- safety (int): Filter the adult content:
    - 0: off
    - 1: medium
    - 2: high
- start_page (int): The page start number
- site (str): Result from given site (www.github.com)
- site_include (bool): True to include parameter 'site' / False to exclude parameter 'site'
- include_word (str): Include a word to the search
- exclude_word (str): Exclude a word to the search
- url_link (str): Contain a link to a particular URL
- inclusive_search_range_start (int): The starting value for a search range
- inclusive_search_range_end (int): The ending value for a search range
- or_operator (str): The results must contain one of the additional search terms
- additional_term (str): To check for additional search terms
- from_date (str): To search from a specific date (d10, w5, m15, ...) (d: day, w: week, m: month, y: year)
- related_url (str): The result should be related to the url (www.github.com)
- client (str): Specify a client
- search_engine_code (str): Unique code that identifies a custom search engine
- boost_country_search (str): Boosts search results whose country of origin matches (uk, es, ...)
- character_encoding_scheme_interpreter (str): Encoding scheme (utf8, latin1, ...)
- character_encoding_scheme_decoder (str): Encoding scheme that should be used to decode the XML result (utf8, latin1, ...)
- output_format (str): Format of the XML results (xml_no_dtd, xml)
- sort (str): Sort by the expression (date, language, ...)
- idn_encoded_url (bool): Display specific character: True (http://www.花井鮨.com) / False (http://www.xn--elq438j.com)
- picture_format (str): Images of a specified type:
  - 'bmp'
  - 'gif'
  - 'png'
  - 'jpg'
  - 'svg'
- picture_size (str): Size of the image:
  - 'icon'
  - 'small'
  - 'medium'
  - 'large'
  - 'xlarge'
  - 'xxlarge'
  - 'huge'
- picture_type (str): Type of the image:
  - 'clipart'
  - 'face'
  - 'lineart'
  - 'news'
  - 'photo'
- picture_color_filter (str): Color filter of the image:
  - 'mono'
  - 'gray'
  - 'color'
- picture_color (str): Color of the image:
  - 'yellow'
  - 'green'
  - 'teal'
  - 'blue'
  - 'purple'
  - 'pink'
  - 'white'
  - 'gray'
  - 'black'
  - 'brown'
- picture_right (str): Liscence of the image:
  - 'cc_publicdomain'
  - 'cc_attribute'
  - 'cc_sharealike'
  - 'cc_noncommercial'
  - 'cc_nonderived'
- dorks_links (list): Should contain all the links ([www.google.com, www.github.com], ...)
- dorks_or (list): Should contain at least of the content
- dorks_theme_exclusion (list): Should exclude all the terms
- dorks_file_type_exclusion (list): Should exclude all the type of files ([PDF, DOC], ...)
- dorks_file_type (list): Should include all the type of files ([PDF, DOC], ...)
- dorks_and (list): Should include all the terms
- dorks_words_in_links (list): Should include all the terms in the links
- dorks_should_appear (list): Should appear in the result
- dorks_related_links (list): All the url should have the similar url patern
- dorks_words_in_text (list): Should contain all the word in the document content
- dorks_word_in_title (list): Should contain a particular word in the document title
- dorks_words_in_title (list): Should contain all the word in the document title
- dorks_word_in_url (list): Should contain a particular word in the url
- dorks_words_in_url (list): Should contain all the word in the url
- dorks_info (list): Retrieves general information about a URL as long as that URL is included in Google's search index
- dorks_cache (list): Show you the cached version of any website (securitytrails.com, ...)
- dorks_anchor (list): Search for an exact anchor text used on any links (cyber security, government, ...)
- dorks_define (list): Search for definitions
- dorks_stocks (list): Search for stocks
- dorks_phonebook (list): Search for phone numbers
- dorks_maps (list): Search for maps
- dorks_book (list): Search for books
- dorks_movie (list): Search for movies
- dorks_site (list): Search for sites
- headers (dict): Header of the query
- proxies (dict): Proxies of the query
- cookies (dict): Cookies of the query
- timeout (int): Delay for the query timeout
- allow_redirects (bool): True to enable / False to disable the redirection on pages
- verify (Any): True to enable / False to disable the verification of ssl_certificate
- stream (Any): Open a stream
- certificate (str): To add a certificate
- request_cooldown (float): Cooldown between each request

To more understand how using the url parameters, here some unittests: https://github.com/Sharkigamers/google_search_origin/blob/master/test.py

For the request parameters, it doesn't differs from the original library.

For more information on the google dorks, here the official google documentation:

https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/csharp/latest/classGoogle_1_1Apis_1_1Customsearch_1_1v1_1_1CseResource_1_1ListRequest-members.html

https://developers.google.com/custom-search/docs/xml_results#clientsp

## Default values

- search_type: 'search'
- base_url: 'www.google.com'
- ssl_certificate: True
- verify: True

Everything else is set to None

## Format to respect

Parameters have specific formats to respect like:

Character Encoding Schemes:
  - 'latin1'
  - 'latin2'
  - 'latin3'
  - 'latin4'
  - 'cyrillic'
  - 'arabic'
  - 'greek'
  - 'hebrew'
  - 'latin5'
  - 'latin6'
  - 'euc-jp'
  - 'euc-kr'
  - 'sjis'
  - 'big5'
  - 'gb'
  - 'utf8'

Country codes:
  - 'af'
  - 'al'
  - 'dz'
  - 'as'
  - 'ad'
  - 'ao'
  - 'ai'
  - 'aq'
  - 'ag'
  - 'ar'
  - 'am'
  - 'aw'
  - 'au'
  - 'at'
  - 'az'
  - 'bs'
  - 'bh'
  - 'bd'
  - 'bb'
  - 'by'
  - 'be'
  - 'bz'
  - 'bj'
  - 'bm'
  - 'bt'
  - 'bo'
  - 'ba'
  - 'bw'
  - 'bv'
  - 'br'
  - 'io'
  - 'bn'
  - 'bg'
  - 'bf'
  - 'bi'
  - 'kh'
  - 'cm'
  - 'ca'
  - 'cv'
  - 'ky'
  - 'cf'
  - 'td'
  - 'cl'
  - 'cn'
  - 'cx'
  - 'cc'
  - 'co'
  - 'km'
  - 'cg'
  - 'cd'
  - 'ck'
  - 'cr'
  - 'ci'
  - 'hr'
  - 'cu'
  - 'cy'
  - 'cz'
  - 'dk'
  - 'dj'
  - 'dm'
  - 'do'
  - 'ec'
  - 'eg'
  - 'sv'
  - 'gq'
  - 'er'
  - 'ee'
  - 'et'
  - 'fk'
  - 'fo'
  - 'fj'
  - 'fi'
  - 'fr'
  - 'gf'
  - 'pf'
  - 'tf'
  - 'ga'
  - 'gm'
  - 'ge'
  - 'de'
  - 'gh'
  - 'gi'
  - 'gr'
  - 'gl'
  - 'gd'
  - 'gp'
  - 'gu'
  - 'gt'
  - 'gn'
  - 'gw'
  - 'gy'
  - 'ht'
  - 'hm'
  - 'va'
  - 'hn'
  - 'hk'
  - 'hu'
  - 'is'
  - 'in'
  - 'id'
  - 'ir'
  - 'iq'
  - 'ie'
  - 'il'
  - 'it'
  - 'jm'
  - 'jp'
  - 'jo'
  - 'kz'
  - 'ke'
  - 'ki'
  - 'kp'
  - 'kr'
  - 'kw'
  - 'kg'
  - 'la'
  - 'lv'
  - 'lb'
  - 'ls'
  - 'lr'
  - 'ly'
  - 'li'
  - 'lt'
  - 'lu'
  - 'mo'
  - 'mk'
  - 'mg'
  - 'mw'
  - 'my'
  - 'mv'
  - 'ml'
  - 'mt'
  - 'mh'
  - 'mq'
  - 'mr'
  - 'mu'
  - 'yt'
  - 'mx'
  - 'fm'
  - 'md'
  - 'mc'
  - 'mn'
  - 'ms'
  - 'ma'
  - 'mz'
  - 'mm'
  - 'na'
  - 'nr'
  - 'np'
  - 'nl'
  - 'an'
  - 'nc'
  - 'nz'
  - 'ni'
  - 'ne'
  - 'ng'
  - 'nu'
  - 'nf'
  - 'mp'
  - 'no'
  - 'om'
  - 'pk'
  - 'pw'
  - 'ps'
  - 'pa'
  - 'pg'
  - 'py'
  - 'pe'
  - 'ph'
  - 'pn'
  - 'pl'
  - 'pt'
  - 'pr'
  - 'qa'
  - 're'
  - 'ro'
  - 'ru'
  - 'rw'
  - 'sh'
  - 'kn'
  - 'lc'
  - 'pm'
  - 'vc'
  - 'ws'
  - 'sm'
  - 'st'
  - 'sa'
  - 'sn'
  - 'cs'
  - 'sc'
  - 'sl'
  - 'sg'
  - 'sk'
  - 'si'
  - 'sb'
  - 'so'
  - 'za'
  - 'gs'
  - 'es'
  - 'lk'
  - 'sd'
  - 'sr'
  - 'sj'
  - 'sz'
  - 'se'
  - 'ch'
  - 'sy'
  - 'tw'
  - 'tj'
  - 'tz'
  - 'th'
  - 'tl'
  - 'tg'
  - 'tk'
  - 'to'
  - 'tt'
  - 'tn'
  - 'tr'
  - 'tm'
  - 'tc'
  - 'tv'
  - 'ug'
  - 'ua'
  - 'ae'
  - 'uk'
  - 'us'
  - 'um'
  - 'uy'
  - 'uz'
  - 'vu'
  - 've'
  - 'vn'
  - 'vg'
  - 'vi'
  - 'wf'
  - 'eh'
  - 'ye'
  - 'zm'
  - 'zw'

Country Collection Values:
  - 'countryAF'
  - 'countryAL'
  - 'countryDZ'
  - 'countryAS'
  - 'countryAD'
  - 'countryAO'
  - 'countryAI'
  - 'countryAQ'
  - 'countryAG'
  - 'countryAR'
  - 'countryAM'
  - 'countryAW'
  - 'countryAU'
  - 'countryAT'
  - 'countryAZ'
  - 'countryBS'
  - 'countryBH'
  - 'countryBD'
  - 'countryBB'
  - 'countryBY'
  - 'countryBE'
  - 'countryBZ'
  - 'countryBJ'
  - 'countryBM'
  - 'countryBT'
  - 'countryBO'
  - 'countryBA'
  - 'countryBW'
  - 'countryBV'
  - 'countryBR'
  - 'countryIO'
  - 'countryBN'
  - 'countryBG'
  - 'countryBF'
  - 'countryBI'
  - 'countryKH'
  - 'countryCM'
  - 'countryCA'
  - 'countryCV'
  - 'countryKY'
  - 'countryCF'
  - 'countryTD'
  - 'countryCL'
  - 'countryCN'
  - 'countryCX'
  - 'countryCC'
  - 'countryCO'
  - 'countryKM'
  - 'countryCG'
  - 'countryCD'
  - 'countryCK'
  - 'countryCR'
  - 'countryCI'
  - 'countryHR'
  - 'countryCU'
  - 'countryCY'
  - 'countryCZ'
  - 'countryDK'
  - 'countryDJ'
  - 'countryDM'
  - 'countryDO'
  - 'countryTP'
  - 'countryEC'
  - 'countryEG'
  - 'countrySV'
  - 'countryGQ'
  - 'countryER'
  - 'countryEE'
  - 'countryET'
  - 'countryEU'
  - 'countryFK'
  - 'countryFO'
  - 'countryFJ'
  - 'countryFI'
  - 'countryFR'
  - 'countryFX'
  - 'countryGF'
  - 'countryPF'
  - 'countryTF'
  - 'countryGA'
  - 'countryGM'
  - 'countryGE'
  - 'countryDE'
  - 'countryGH'
  - 'countryGI'
  - 'countryGR'
  - 'countryGL'
  - 'countryGD'
  - 'countryGP'
  - 'countryGU'
  - 'countryGT'
  - 'countryGN'
  - 'countryGW'
  - 'countryGY'
  - 'countryHT'
  - 'countryHM'
  - 'countryVA'
  - 'countryHN'
  - 'countryHK'
  - 'countryHU'
  - 'countryIS'
  - 'countryIN'
  - 'countryID'
  - 'countryIR'
  - 'countryIQ'
  - 'countryIE'
  - 'countryIL'
  - 'countryIT'
  - 'countryJM'
  - 'countryJP'
  - 'countryJO'
  - 'countryKZ'
  - 'countryKE'
  - 'countryKI'
  - 'countryKP'
  - 'countryKR'
  - 'countryKW'
  - 'countryKG'
  - 'countryLA'
  - 'countryLV'
  - 'countryLB'
  - 'countryLS'
  - 'countryLR'
  - 'countryLY'
  - 'countryLI'
  - 'countryLT'
  - 'countryLU'
  - 'countryMO'
  - 'countryMK'
  - 'countryMG'
  - 'countryMW'
  - 'countryMY'
  - 'countryMV'
  - 'countryML'
  - 'countryMT'
  - 'countryMH'
  - 'countryMQ'
  - 'countryMR'
  - 'countryMU'
  - 'countryYT'
  - 'countryMX'
  - 'countryFM'
  - 'countryMD'
  - 'countryMC'
  - 'countryMN'
  - 'countryMS'
  - 'countryMA'
  - 'countryMZ'
  - 'countryMM'
  - 'countryNA'
  - 'countryNR'
  - 'countryNP'
  - 'countryNL'
  - 'countryAN'
  - 'countryNC'
  - 'countryNZ'
  - 'countryNI'
  - 'countryNE'
  - 'countryNG'
  - 'countryNU'
  - 'countryNF'
  - 'countryMP'
  - 'countryNO'
  - 'countryOM'
  - 'countryPK'
  - 'countryPW'
  - 'countryPS'
  - 'countryPA'
  - 'countryPG'
  - 'countryPY'
  - 'countryPE'
  - 'countryPH'
  - 'countryPN'
  - 'countryPL'
  - 'countryPT'
  - 'countryPR'
  - 'countryQA'
  - 'countryRE'
  - 'countryRO'
  - 'countryRU'
  - 'countryRW'
  - 'countrySH'
  - 'countryKN'
  - 'countryLC'
  - 'countryPM'
  - 'countryVC'
  - 'countryWS'
  - 'countrySM'
  - 'countryST'
  - 'countrySA'
  - 'countrySN'
  - 'countryCS'
  - 'countrySC'
  - 'countrySL'
  - 'countrySG'
  - 'countrySK'
  - 'countrySI'
  - 'countrySB'
  - 'countrySO'
  - 'countryZA'
  - 'countryGS'
  - 'countryES'
  - 'countryLK'
  - 'countrySD'
  - 'countrySR'
  - 'countrySJ'
  - 'countrySZ'
  - 'countrySE'
  - 'countryCH'
  - 'countrySY'
  - 'countryTW'
  - 'countryTJ'
  - 'countryTZ'
  - 'countryTH'
  - 'countryTG'
  - 'countryTK'
  - 'countryTO'
  - 'countryTT'
  - 'countryTN'
  - 'countryTR'
  - 'countryTM'
  - 'countryTC'
  - 'countryTV'
  - 'countryUG'
  - 'countryUA'
  - 'countryAE'
  - 'countryUK'
  - 'countryUS'
  - 'countryUM'
  - 'countryUY'
  - 'countryUZ'
  - 'countryVU'
  - 'countryVE'
  - 'countryVN'
  - 'countryVG'
  - 'countryVI'
  - 'countryWF'
  - 'countryEH'
  - 'countryYE'
  - 'countryYU'
  - 'countryZM'
  - 'countryZW'

Filters:
  - 'app'
  - 'blg'
  - 'bks'
  - 'dsc'
  - 'isch'
  - 'nws'
  - 'pts'
  - 'plcs'
  - 'rcp'
  - 'shop'
  - 'vid'

Language Collection Values:
  - 'lang_ar'
  - 'lang_bg'
  - 'lang_ca'
  - 'lang_zh-CN'
  - 'lang_zh-TW'
  - 'lang_hr'
  - 'lang_cs'
  - 'lang_da'
  - 'lang_nl'
  - 'lang_en'
  - 'lang_et'
  - 'lang_fi'
  - 'lang_fr'
  - 'lang_de'
  - 'lang_el'
  - 'lang_iw'
  - 'lang_hu'
  - 'lang_is'
  - 'lang_id'
  - 'lang_it'
  - 'lang_ja'
  - 'lang_ko'
  - 'lang_lv'
  - 'lang_lt'
  - 'lang_no'
  - 'lang_pl'
  - 'lang_pt'
  - 'lang_ro'
  - 'lang_ru'
  - 'lang_sr'
  - 'lang_sk'
  - 'lang_sl'
  - 'lang_es'
  - 'lang_sv'
  - 'lang_tr'

Picture Format:
  - 'bmp'
  - 'gif'
  - 'png'
  - 'jpg'
  - 'svg'

Picture Size:
  - 'icon'
  - 'small'
  - 'medium'
  - 'large'
  - 'xlarge'
  - 'xxlarge'
  - 'huge'

Picture type
  - 'clipart'
  - 'face'
  - 'lineart'
  - 'news'
  - 'photo'

Picture Color Filter
  - 'mono'
  - 'gray'
  - 'color'

Picture color
  - 'yellow'
  - 'green'
  - 'teal'
  - 'blue'
  - 'purple'
  - 'pink'
  - 'white'
  - 'gray'
  - 'black'
  - 'brown'

Picture Right
  - 'cc_publicdomain'
  - 'cc_attribute'
  - 'cc_sharealike'
  - 'cc_noncommercial'
  - 'cc_nonderived'

Ouput Format:
  - 'xml_no_dtd'
  - 'xml'