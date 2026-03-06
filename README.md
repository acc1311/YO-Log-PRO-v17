# 📻 YO Log PRO v17 — CAT Edition

### Logger Profesional pentru Concursuri de Radioamatorism
### Professional Multi-Contest Amateur Radio Logger

[![Build Status](../../actions/workflows/build.yml/badge.svg)](../../actions/workflows/build.yml)
[![Release](../../releases/latest/badge.svg)](../../releases/latest)

---

## 📥 Descărcare / Download

Mergi la [**Releases**](../../releases) și descarcă `YO_Log_PRO_v17.exe`

> ✅ **Nu necesită instalare Python** — executabil standalone (~12 MB)
> ✅ **Construit cu Python 3.8.10 — compatibil Windows 7 SP1+**
> ⚠️ **Windows 7/8**: Instalează [vcredist\_x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe) dacă apare eroare DLL

---

## 🖥️ COMPATIBILITATE / COMPATIBILITY

| Sistem / System | Status | Note |
|----------------|--------|------|
| Windows 7 SP1 (32/64 bit) | ✅ | Necesită vcredist |
| Windows 8 / 8.1 | ✅ | |
| Windows 10 | ✅ | |
| Windows 11 | ✅ | |

> **Build cu Python 3.8.10** — ultima versiune oficială compatibilă cu Windows 7.

---

## 🆕 NOU ÎN v17 / NEW IN v17

### 📡 CAT — Computer Aided Transceiver (NOU!)

Frecvența și modul de lucru se citesc **automat** din transceiver și se completează în log!

#### Protocoale suportate:

| Protocol | Radio-uri compatibile |
|----------|-----------------------|
| **Yaesu CAT** | FT-891, FT-991A, FT-817ND, FT-857D, FT-450D, FT-950, FT-DX10, FT-DX3000 |
| **Icom CI-V** | IC-7300, IC-705, IC-9700, IC-7100, IC-7600, IC-7700, IC-7850, IC-718 |
| **Kenwood CAT** | TS-590S/SG, TS-2000, TS-480, TS-890S, TS-990S |
| **Elecraft CAT** | K3, K3S, KX3, KX2, K4 |
| **Hamlib/rigctld** | **400+ radio-uri** via daemon extern |
| **Manual** | Fără CAT — funcționare normală |

#### Funcționalități CAT:
- 🔄 **Citire automată** frecvență + mod din radio la **2 secunde**
- ↔️ **Bidirecțional** — schimbi banda/modul în program → se trimite automat spre radio
- ⌨️ **Enter în câmpul Freq** → trimite frecvența spre radio
- 📡 **Indicator CAT în header** — verde = conectat, roșu = deconectat (click = setări)
- 🔌 **Reconectare automată** la pornirea programului
- 🔍 **Auto-detectare porturi COM** cu buton refresh

#### Configurare CAT — FT-891 (exemplu):
```
Protocol:  Yaesu CAT
Port COM:  COM3  (verifică în Device Manager)
Baud Rate: 38400
→ Conectează
```

#### Configurare CAT — IC-7300 (exemplu):
```
Protocol:   Icom CI-V
Port COM:   COM4
Baud Rate:  19200
CI-V Addr:  94  (hex)
→ Conectează
```

#### Configurare Hamlib (orice radio):
```bash
# Instalează Hamlib: https://hamlib.github.io
# Pornește rigctld:
rigctld -m 122 -r COM3 -s 38400    # Yaesu FT-891 (model 122)
rigctld -m 3061 -r COM4 -s 19200   # Icom IC-7300 (model 3061)
rigctld -m 229 -r COM5 -s 9600     # Kenwood TS-590 (model 229)

# În YO Log PRO:
Protocol:  Hamlib/rigctld
Host:      localhost
Port:      4532
```

> Lista completă modele Hamlib: `rigctld --list`

---

### ⏱ Timer Concurs Îmbunătățit

- ✅ Durata în **ore SAU minute**
- ✅ Avertizare sonoră la **5 minute** rămase (galben + 2 beep-uri)
- ✅ Avertizare sonoră la **1 minut** rămas (roșu + 3 beep-uri)
- ✅ Beep triplu la **TIME UP** — mesaj roșu pe ecran
- ✅ Checkbox activare/dezactivare sunete timer

### 📝 Log Nou

- ✅ Creare log nou cu **nume personalizat** — păstrează logurile vechi
- ✅ Alegi concursul din listă
- ✅ Logul curent se **salvează automat** înainte
- ✅ Accesibil din meniu `📝 Log` și buton jos

### 🎨 Teme și Culori

| Temă | Stil |
|------|------|
| Dark Blue (implicit) | Negru + albastru |
| Dark Green | Negru + verde |
| Dark Red | Negru + roșu |
| Dark Purple | Negru + violet |
| Light (Zi) | Alb + albastru |
| Light Sepia | Crem + maro |

- ✅ **Editor culori custom** — dublu-click pe orice culoare
- ✅ **Preview live** înainte să aplici
- ✅ Tema se salvează automat

---

## 💾 BACKUP AUTOMAT / AUTO BACKUP

| Eveniment | Când |
|-----------|------|
| **Autosave** log | La fiecare **60 secunde** |
| La **ieșire** | La fiecare închidere |
| Înainte de **export** | Cabrillo, ADIF, EDI, CSV |
| La **golire log** | Înainte de ștergere |

```
📁 folderul programului\
└── backups\
    ├── log_simplu_20260305_143022.json
    └── ... (maxim 50 per concurs)
```

---

## 📋 FUNCȚIONALITĂȚI COMPLETE

### 🇷🇴 Operare rapidă

```
PRIMUL QSO:
1. [📡 CAT conectat] → Freq și Mod se completează automat din radio
2. Tastați indicativul → YO3ABC
3. ENTER → QSO logat!

FĂRĂ CAT:
1. Setați banda → 40m  (sau F2 pentru bandă următoare)
2. Setați modul → SSB  (sau F3 pentru mod următor)
3. Tastați indicativul → ENTER → LOG!

SCHIMBAȚI FRECVENȚA DIN PROGRAM:
1. Scrieți frecvența în câmpul Freq → 14.200
2. ENTER → se trimite spre radio via CAT
```

### 🇬🇧 Quick Flow

```
WITH CAT: Freq + Mode auto-filled from radio → type callsign → ENTER
WITHOUT CAT: F2=Band, F3=Mode → type callsign → ENTER → LOG!
```

---

## 📤 EXPORTURI / EXPORTS

| Format | Descriere |
|--------|-----------|
| **Cabrillo 3.0** (.log) | Standard internațional |
| **Cabrillo 2.0** (.log) | Cu dialog configurare exchange |
| **ADIF 3.1** (.adi) | Universal |
| **CSV** (.csv) | Excel |
| **EDI / REG1TEST** (.edi) | VHF/UHF european |
| **Print** (.txt) | Raport text |

## 📥 IMPORTURI / IMPORTS

ADIF · CSV · Cabrillo 2.0 · Cabrillo 3.0

---

## 🔧 TASTE RAPIDE / SHORTCUTS

| Tastă | Acțiune |
|-------|---------|
| **Enter** | LOG QSO |
| **F2** | Bandă următoare |
| **F3** | Mod următor |
| **Ctrl+S** | Salvare forțată |
| **Ctrl+Z** | Undo |
| **Ctrl+F** | Căutare în log |
| **Enter (în Freq)** | Trimite frecvența spre radio |

---

## 🐛 DEPANARE / TROUBLESHOOTING

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| „This app can't run on your PC" | Python 3.9+ build | Folosește această versiune ✅ |
| Eroare DLL la pornire | Visual C++ lipsă | Instalează vcredist_x64.exe |
| CAT: port nu apare | Driver neinstalat | Instalează driver USB-Serial |
| CAT: fără răspuns | Baud greșit | Verifică baud în meniul radio |
| CAT: Icom no response | CI-V address greșit | Verifică adresa în meniul radio |
| Hamlib: connection refused | rigctld nu rulează | Pornește rigctld mai întâi |

### Driver-e USB-Serial frecvente:
- **CH340/CH341** (multe cabluri ieftine): [driver CH340](https://www.wch-ic.com/downloads/CH341SER_EXE.html)
- **CP2102** (Silicon Labs): [driver CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
- **FTDI** (FT232): [driver FTDI](https://ftdichip.com/drivers/vcp-drivers/)

---

## 🔨 BUILD LOCAL

```bash
# 1. Instalează Python 3.8.10
# https://www.python.org/downloads/release/python-3810/

# 2. Instalează dependențe
pip install -r requirements.txt

# 3. Rulează direct (fără build)
python yo_log_pro.py

# 4. Build EXE
pyinstaller YO_Log_PRO_v17.spec
# sau
pyinstaller --onefile --windowed --name YO_Log_PRO_v17 --icon icon.ico yo_log_pro.py
```

---

## 📜 CHANGELOG

### v17.0 — CAT Edition
- ✅ **NOU:** CAT bidirecțional — Yaesu / Icom / Kenwood / Elecraft / Hamlib
- ✅ **NOU:** Indicator CAT în header cu status live
- ✅ **NOU:** Enter în Freq → trimite spre radio
- ✅ **NOU:** Timer cu ore/minute și avertizări sonore
- ✅ **NOU:** Log Nou cu nume personalizat
- ✅ **NOU:** 6 teme + editor culori custom
- ✅ **NOU:** pyserial inclus în EXE (--hidden-import)

### v16.5
- ✅ FIX: Freq/Band/Mode/RST persistă între QSO-uri
- ✅ Export Cabrillo 2.0 cu dialog exchange configurabil

### v16.4
- ✅ Import Cabrillo 2.0 și 3.0
- ✅ Preview dialog pentru exporturi
- ✅ Backup automat înainte de export

---

## 📞 CONTACT

| | |
|---|---|
| **Dezvoltator** | Ardei Constantin-Cătălin |
| **Indicativ** | **YO8ACR** |
| **Email** | yo8acr@gmail.com |
| **Repository v17** | https://github.com/acc1311/YO-Log-PRO-v17 |
| **Repository v16** | https://github.com/acc1311/YO-Log-PRO |

---

**73 de YO8ACR! 📻**
*"v17 — CAT Edition: Transceiver-ul și loggerul vorbesc aceeași limbă!"*
