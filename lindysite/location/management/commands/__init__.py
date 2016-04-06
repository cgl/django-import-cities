city_types = ['PPL', 'PPLA', 'PPLC', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLG']
baseurl="http://download.geonames.org/export/dump/"
files = {
    'country': {
        'filename': 'countryInfo.txt',
        'fields': [
            'code',
            'code3',
            'codeNum',
            'fips',
            'name',
            'capital',
            'area',
            'population',
            'continent',
            'tld',
            'currencyCode',
            'currencyName',
            'phone',
            'postalCodeFormat',
            'postalCodeRegex',
            'languages',
            'geonameid',
            'neighbours',
            'equivalentFips'
        ]
    },
    'city': {
        'filename': 'cities5000.txt',
        'zipfilename': 'cities5000.zip',
        'fields': [
            'geonameid',
            'name',
            'asciiName',
            'alternateNames',
            'latitude',
            'longitude',
            'featureClass',
            'featureCode',
            'countryCode',
            'cc2',
            'admin1Code',
            'admin2Code',
            'admin3Code',
            'admin4Code',
            'population',
            'elevation',
            'gtopo30',
            'timezone',
            'modificationDate'
        ]
    },
    'region': {
        'filename': 'admin1CodesASCII.txt',
        'fields': [
            'code',
            'name',
            'asciiName',
            'geonameid',
        ]
    },
    'subregion': {
        'filename': 'admin2Codes.txt',
        'fields': [
            'code',
            'name',
            'asciiName',
            'geonameid',
        ]
    },

}
