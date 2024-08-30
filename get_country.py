import requests
from bs4 import BeautifulSoup
def get_country():
    country_url = 'https://www.numbeo.com/quality-of-life/'
    response = requests.get(country_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    country_soup = soup.find_all(name='option')
    all_countries = [country.text for country in country_soup]
    all_countries.pop(0)
    return all_countries