# Simulator temperatură și saturație – Proiect

Acest script (`simulator.py`) generează date aleatorii de temperatură și saturație pentru un pacient și le salvează într-o bază de date MySQL.

## 📦 Ce face:
- Generează valori aleatorii la 5 secunde
- Salvează în tabelele:
  - `temperatures(patient_id, value, timestamp)`
  - `saturations(patient_id, value, timestamp)`

## 🛠 Configurare:
1. Instalează pachetele:
```
pip install -r requirements.txt
```

2. Editează fișierul `db_config.py` cu datele tale MySQL.

3. Rulează simulatorul:
```
python simulator.py
```

## 🧩 Legături viitoare:
- API Flask citește aceste date (pasul 2)
- Interfața web afișează alerte
- Blockchain primește valorile periculoase
