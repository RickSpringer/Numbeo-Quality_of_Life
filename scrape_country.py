import requests
from bs4 import BeautifulSoup

def scrape_ql_country(country_name: str):
    # building link
    base_ql_url = 'https://www.numbeo.com/'
    joined_link = ''.join([base_ql_url, '/quality-of-life/country_result.jsp?country=', country_name]).replace(' ', '+')

    # Getting city ql for country
    try:
        response = requests.get(joined_link)
        response.encoding = 'utf-8'
        country_soup = BeautifulSoup(response.text, 'html.parser')
        if country_soup.find_all(name="table")[4]:
            soup = country_soup.find_all(name="table")[4]
            return soup

        else:
            print(f'Keine ausreichenden Daten zu {country_name} verfügbar.')

    except Exception as e:
        print(f'Keine ausreichenden Daten zu {country_name} verfügbar.')
        print(e)
