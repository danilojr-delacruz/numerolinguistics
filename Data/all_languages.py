import pandas as pd

for language in ['Danish', 'Dutch', 'English', 'Finnish', 'French', 'German',
                 'Italian', 'Latin', 'Portuguese', 'Spanish', 'Swedish']:
    print(language)
    url = f"https://www.lexisrex.com/{language}-Numbers/1-100"

    table = pd.read_html(url, match='Number')[1]

    list_of_nums = table[language].to_list()[1:]

    f = open(f'{language.lower()}.txt', 'w')
    f.write(','.join(list_of_nums))
    f.close()