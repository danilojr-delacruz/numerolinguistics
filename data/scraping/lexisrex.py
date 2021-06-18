import pandas as pd


from unidecode import unidecode


for language in ['Chinese', 'Danish', 'Dutch', 'English', 'Finnish', 'French', 
                 'German', 'Greek', 'Italian', 'Russian', 'Latin', 
                 'Portuguese', 'Spanish', 'Swedish']:
    print(language)

    url = f"https://www.lexisrex.com/{language}-Numbers/1-100"
    table = pd.read_html(url, match='Number')[1]
    list_of_nums = table[language].to_list()[1:]

    with open(f'{language.lower()}.txt', 'w') as f:
        f.write('\n'.join([unidecode(n) for n in list_of_nums]))
