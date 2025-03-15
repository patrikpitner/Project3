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
    
    soup = BeautifulSoup(odpoved.text, 'html.parser')
    
    return soup

def seznam_obci(url):
    soup = stahni_stranku(url)
    
    obce = []
    
    for radek in soup.select("table.table tr")[2:]:
        bunky = radek.find_all('td')
        
        if len(bunky) >= 3 and bunky[0].find('a'):
            obec = {
                'kod': bunky[0].text.strip(),
                'nazev': bunky[1].text.strip(),
                'url': 'https://www.volby.cz/pls/ps2017nss/' + bunky[0].find('a')['href']
            }
            
            obce.append(obec)
    
    return obce

def ziskej_data(url_obce):
    soup = stahni_stranku(url_obce)
    
    try:
        registrovani = int(soup.select('td.cislo')[3].text.replace('\xa0', ''))
        obalky = int(soup.select('td.cislo')[4].text.replace('\xa0', ''))
        platne = int(soup.select('td.cislo')[7].text.replace('\xa0', ''))
    except (IndexError, ValueError):
        return None
    
    strany = []
    hlasy = []
    
    for tabulka in soup.select('div.t2_470 table'):
        for radek in tabulka.select('tr')[2:]:
            bunky = radek.find_all('td')
            
            if len(bunky) >= 4:
                try:
                    pocet_hlasu = int(bunky[2].text.replace('\xa0', ''))
                except ValueError:
                    continue
                
                strany.append(bunky[1].text.strip())
                hlasy.append(pocet_hlasu)
    
    return registrovani, obalky, platne, hlasy, strany

def uloz_data(url, vystup):
    obce = seznam_obci(url)
    
    data = []
    hlavicka = []
    
    for index, obec in enumerate(obce):
        vysledky = ziskej_data(obec['url'])
        
        if vysledky:
            reg, obal, plat, hlasy, strany = vysledky
            
            if index == 0:
                hlavicka = ['kod', 'nazev', 'registrovani', 'obalky', 'platne'] + strany
            
            radek = [
                obec['kod'],
                obec['nazev'],
                reg,
                obal,
                plat
            ] + hlasy
            
            data.append(radek)
    
    df = pd.DataFrame(data, columns=hlavicka)
    df.to_csv(vystup, index=False, encoding='utf-8-sig')
    
    print(f"Data ulozena do {vystup}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python main.py <URL> <vystup.csv>")
        sys.exit(1)
    
    url = sys.argv[1]
    vystup = sys.argv[2]
    
    uloz_data(url, vystup)
