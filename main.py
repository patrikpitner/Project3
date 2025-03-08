"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Patrik Pitner
email: patrikpitner@seznam.cz
"""
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

def stahni_stranku(url):
    odpoved = requests.get(url)
    odpoved.encoding = 'utf-8'
    return BeautifulSoup(odpoved.text, 'html.parser')

def seznam_obci(url):
    soup = stahni_stranku(url)
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

def data_obce(url_obce):
    soup = stahni_stranku(url_obce)
    registered = int(soup.select('td.cislo')[3].text.replace('\xa0', ''))
    envelopes = int(soup.select('td.cislo')[4].text.replace('\xa0', ''))
    valid = int(soup.select('td.cislo')[7].text.replace('\xa0', ''))
    strany = []
    hlasy = []
    for tabulka in soup.select('div.t2_470 table'):
        radky_stran = tabulka.select('tr')[2:]
        for radek_strany in radky_stran:
            bunky = radek_strany.find_all('td')
            if len(bunky) >= 4:
                try:
                    pocet_hlasu = int(bunky[2].text.replace('\xa0', ''))
                except ValueError:
                    continue
                strany.append(bunky[1].text.strip())
                hlasy.append(pocet_hlasu)
    return registered, envelopes, valid, hlasy, strany

def priprav_data(url):
    obce = seznam_obci(url)
    data = []
    hlavicka = []
    for index, obec in enumerate(obce):
        reg, env, val, hlasy, strany = data_obce(obec['url'])
        if index == 0:
            hlavicka = ['code', 'location', 'registered', 'envelopes', 'valid'] + strany
        data.append([obec['code'], obec['location'], reg, env, val] + hlasy)
    return hlavicka, data

def uloz_csv(url, vystup):
    hlavicka, data = priprav_data(url)
    df = pd.DataFrame(data, columns=hlavicka)
    df.to_csv(vystup, index=False, encoding='utf-8-sig')
    print(f"Data byla uložena do {vystup}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python main.py <URL> <vystup.csv>")
        sys.exit(1)
    url = sys.argv[1]
    vystupni_soubor = sys.argv[2]
    uloz_csv(url, vystupni_soubor)
