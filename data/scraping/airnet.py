import pandas as pd


from unidecode import unidecode


for language in ['ainu', 'alamblak', 'arabic', 'assyrian', 'aymara', 'basque',
                 'estonian', 'chinook_wawa', 'croatian', 'cuzco_quechua',
                 'esperanto', 'ganda', 'georgian', 'hawaiian', 'hindi',
                 'huli', 'hungarian', 'indonesian', 'javanese', 'kiribati',
                 'maltese', 'manx', 'nahuatl', 'ndom', 'norwegian', 'ojibwa',
                 'romanian', 'swahili', 'thai', 'vietnamese', 'wolof',
                 'yoruba', 'zulu']:
    print(language)

    url = f"http://www.sf.airnet.ne.jp/~ts/language/number/{language}.html"
    table = pd.read_html(url, match='Reading')[0]
    list_of_nums = table.iloc[:,1].fillna('?').to_list()

    with open(f'{language.lower()}.txt', 'w') as f:
        f.write('\n'.join([unidecode(n) for n in list_of_nums]))
