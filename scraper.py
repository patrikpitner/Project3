"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie"

author: Patrik Pitner
email: patrikpitner@seznam.cz
"""
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

def ziskej_obsah(url):
    odpoved = requests.get(url)
    odpoved.encoding = 'utf-8'
    return BeautifulSoup(odpoved.text, 'html.parser')

def ziskej_obce(url):
    soup = ziskej_obsah(url)
    obce = []
    for radek in soup.select("table.table tr")[2:]:
        bunky = radek.find_all('td')
        if len(bunky) >= 3 and bunky[0].find('a'):
            obce.append({
                'code': bunky[0].text.strip(),
                'location': bunky[1].text.strip(),
                'url': 'https://www.volby.cz/pls/ps2017nss/' + bunky[0].find('a')['href']
            })
    return obce

def ziskej_data_obce(url):
    soup = ziskej_obsah(url)
    registered = int(soup.select('td.cislo')[3].text.replace('\xa0', ''))
    envelopes = int(soup.select('td.cislo')[4].text.replace('\xa0', ''))
    valid = int(soup.select('td.cislo')[7].text.replace('\xa0', ''))

    strany = []
    hlasy = []

    for tab in soup.select('div.t2_470 table'):
        strany += [x.text for x in tab.select('td.overflow_name')]
        cisla = tab.select('td.cislo')
        hlasy += [int(cisla[i].text.replace('\xa0', '')) for i in range(0, len(cisla), 2)]

    return registered, envelopes, valid, hlasy, strany

def priprav_data_pro_csv(url):
    obce = ziskej_obce(url)
    data = []

    for idx, obec in enumerate(obce):
        registered, envelopes, valid, hlasy, strany = ziskej_data_obce(obec['url'])
        if idx == 0:
            hlavicka = ['code', 'location', 'registered', 'envelopes', 'valid'] + strany
        radek = [obec['code'], obec['location'], registered, envelopes, valid] + hlasy
        data.append(radek)

    return hlavicka, data

def uloz_csv(url, vystupni_soubor):
    hlavicka, data = priprav_data_pro_csv(url)
    df = pd.DataFrame(data, columns=hlavicka)
    df.to_csv(vystupni_soubor, index=False, encoding='utf-8-sig')
    print(f'Data byla úspěšně uložena do souboru: {vystupni_soubor}')

def priprav_data_pro_csv(url):
    obce = ziskej_obce(url)
    data = []

    for idx, obec in enumerate(obce):
        registered, envelopes, valid, hlasy, strany = ziskej_data_obce(obec['url'])
        if idx == 0:
            hlavicka = ['code', 'location', 'registered', 'envelopes', 'valid'] + strany
        radek = [obec['code'], obec['location'], registered, envelopes, valid] + hlasy
        data.append(radek)

    return hlavicka, data

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python scraper.py <URL> <výstupní_soubor.csv>")
        sys.exit(1)

    url, vystupni_soubor = sys.argv[1], sys.argv[2]
    uloz_csv(url, vystupni_soubor)
