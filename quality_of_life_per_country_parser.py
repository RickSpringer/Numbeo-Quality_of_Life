import numpy as np
from scrape_country import scrape_ql_country


def parse_table(table_data):
    try:
        # Tabellentitel in table_title speichern
        table_title_soup = table_data.find_all('th')
        table_title = [t.text for t in table_title_soup]
        if 'Rank' in table_title:
            table_title.remove('Rank')

        # mit Titeln table_dict bauen
        table_dict = dict.fromkeys(table_title)
        for key in table_dict:
            table_dict[key] = []

        # Tabelle auslesen und Werte in Listen speichern
        all_tds = []
        soup_rows = table_data.find_all('tr')[1:]
        for row in soup_rows:
            td = row.find_all('td')[1:]
            td_list = [td2.text for td2 in td]
            all_tds.append(td_list)

        # Listen zu Arrays konvertieren und transposieren
        city_array = np.array(all_tds)
        city_array_transposed = city_array.transpose()

        # Array und Dict zusammenzippen
        city_dict = {}

        # Array und Dict zusammenzippen
        city_tuples = [(key, value) for i, (key, value) in
                       enumerate(zip(table_title, city_array_transposed))]
        for key, value in city_tuples:
            city_dict[key] = value
        return city_dict

    except Exception as e:
        print(f'Keine parsing möglich')
        print(e)
