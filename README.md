# Universal Voting Scraper

Tento skript umožňuje automatické stahování a zpracování volebních dat z webových stránek [volby.cz](https://www.volby.cz) a jejich uložení do CSV souboru.

---

## 📌 Požadavky

Před spuštěním skriptu se ujisti, že máš nainstalované následující knihovny:

```bash
pip install requests pandas beautifulsoup4
```

Doporučujeme používat **virtuální prostředí**:

```bash
python -m venv venv  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

---

## 🚀 Spuštění skriptu

### **Na Windows:**

1. **Otevři PowerShell nebo CMD.**
2. **Přesuň se do složky**, kde je uložený `main.py`:
   ```powershell
   cd "C:\Users\TvojeUživatelskéJméno\Desktop\Projekt3"
   ```
3. **Spusť skript** se dvěma argumenty (URL a výstupní soubor):
   ```powershell
   python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vysledky_karlovyvary.csv"
   ```

### **Na macOS/Linux:**

1. **Otevři Terminál.**
2. **Přesuň se do složky**, kde je uložený `main.py`:
   ```bash
   cd "/Users/TvojeUživatelskéJméno/Desktop/Projekt3"
   ```
3. **Spusť skript** se dvěma argumenty (URL a výstupní soubor):
   ```bash
   python3 main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4102" "vysledky_karlovyvary.csv"
   ```

---

## 📂 Výstupní CSV soubor

CSV soubor obsahuje následující sloupce:

- `kod` – Kód obce  
- `nazev` – Název obce  
- `registrovani` – Počet registrovaných voličů  
- `obalky` – Počet odevzdaných obálek  
- `platne` – Počet platných hlasů  
- `+ jednotlivé strany a jejich hlasy`

---

## ❌ Možné chyby a jejich řešení

### ❗ Chyba: "No such file or directory: 'main.py'"
✅ **Ujisti se, že jsi ve správné složce:**

#### **Na Windows:**
```powershell
cd "C:\Users\TvojeUživatelskéJméno\Desktop\Projekt3"
```

#### **Na macOS/Linux:**
```bash
cd "/Users/TvojeUživatelskéJméno/Desktop/Projekt3"
```

Pokud stále soubor není nalezen, ověř existenci skriptu příkazem:
```bash
ls   # macOS/Linux
```
```powershell
Get-ChildItem  # Windows
```

---

### ❗ Chyba: "ModuleNotFoundError: No module named 'requests'"
✅ **Nainstaluj chybějící knihovny:**
```bash
pip install requests pandas beautifulsoup4
```

---

### ❗ Chyba: "Can't open file '\*\*\*\*'"
✅ **Ujisti se, že voláš skript správně:**
```bash
python main.py "URL" "vystup.csv"   # Windows
python3 main.py "URL" "vystup.csv"  # macOS/Linux
```

---

## 🔚 Ukončení virtuálního prostředí

Po dokončení práce doporučujeme deaktivovat virtuální prostředí:

### **Na Windows:**
```powershell
venv\Scripts\deactivate
```

### **Na macOS/Linux:**
```bash
deactivate
```

---

## 📞 Kontakt

Pokud narazíš na problém nebo máš dotaz, neváhej se ozvat! 😊
