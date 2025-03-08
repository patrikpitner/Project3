# Project3 Scraper výsledků parlamentních voleb 2017
Pro macOS

Tento skript automaticky stáhne výsledky parlamentních voleb České republiky za rok 2017 pro konkrétní územní celek z oficiálních stránek www.volby.cz.

Instalace

Doporučuji vytvořit nové virtuální prostředí a nainstalovat závislosti pomocí:

python -m venv env
source env/bin/activate
pip install -r requirements.txt

Jak spustit?

Skript vyžaduje dva argumenty:

URL stránky s územním celkem

Název výstupního CSV souboru

Spuštění skriptu:

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"

Výsledkem bude CSV soubor se strukturou:

code: Kód obce

location: Název obce

registered: Počet voličů v seznamu

envelopes: Počet vydaných obálek

valid: Počet platných hlasů

Jednotlivé sloupce kandidujících stran obsahující absolutní počty hlasů

Ukázka použití

python scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"

Výsledkem bude soubor vysledky_benesov.csv s kompletními výsledky pro Benešov.

Potřebné knihovny:

requests

beautifulsoup4

pandas
