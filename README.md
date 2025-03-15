📊 Universal Voting Scraper
Tento skript slouží ke stahování a zpracování volebních dat z webových stránek volby.cz a jejich následnému uložení do CSV souboru.

📌 Požadavky
Před spuštěním skriptu se ujisti, že máš nainstalované následující knihovny:
pip install requests pandas beautifulsoup4

🚀 Spuštění skriptu
Na Windows:
Otevři PowerShell nebo CMD.
Přesuň se do složky, kde je uložený main.py: cd "C:\Users\TvojeUživatelskéJméno\Desktop\Projekt3"
Spusť skript se dvěma argumenty (URL a výstupní soubor): python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vysledky_karlovyvary.csv"
Na macOS/Linux:
Otevři Terminál.
Přesuň se do složky, kde je uložený main.py: cd "/Users/TvojeUživatelskéJméno/Desktop/Projekt3"
Spusť skript se dvěma argumenty (URL a výstupní soubor): python3 main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vysledky_karlovyvary.csv"

📂 Výstupní CSV soubor
CSV soubor obsahuje následující sloupce:
kod – Kód obce
nazev – Název obce
registrovani – Počet registrovaných voličů
obalky – Počet odevzdaných obálek
platne – Počet platných hlasů
+ jednotlivé strany a jejich hlasy

❌ Možné chyby a jejich řešení
🔴 Chyba: "No such file or directory: 'main.py'"
✅ Ujisti se, že jsi ve správné složce:
Na Windows:
cd "C:\Users\TvojeUživatelskéJméno\Desktop\Projekt3"
Na macOS/Linux:
cd "/Users/TvojeUživatelskéJméno/Desktop/Projekt3"
Pokud stále soubor není nalezen, ověř existenci skriptu příkazem:
ls   # macOS/Linux
Get-ChildItem  # Windows
🔴 Chyba: "ModuleNotFoundError: No module named 'requests'"
✅ Nainstaluj chybějící knihovny:
pip install requests pandas beautifulsoup4
🔴 Chyba: "Can't open file '****'"
✅ Ujisti se, že voláš skript správně:
python main.py "URL" "vystup.csv"   # Windows
python3 main.py "URL" "vystup.csv"  # macOS/Linux

🔚 Ukončení virtuálního prostředí
Po dokončení práce doporučujeme deaktivovat virtuální prostředí:
Na Windows:
venv\Scripts\deactivate
Na macOS/Linux:
deactivate

📞 Kontakt
Pokud narazíš na problém nebo máš dotaz, neváhej se ozvat! 😊
