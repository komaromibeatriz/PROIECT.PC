import random
import time
from datetime import datetime
import mysql.connector
from db_config import DB_CONFIG

def genereaza_temperatura():
    return round(random.uniform(35.5, 37.2), 2)

def genereaza_saturatie():
    return random.randint(88, 99)

def salveaza_in_baza(temp, sat, patient_id=1):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO temperatures (patient_id, value, timestamp) VALUES (%s, %s, %s)",
            (patient_id, temp, datetime.now())
        )
        cursor.execute(
            "INSERT INTO saturations (patient_id, value, timestamp) VALUES (%s, %s, %s)",
            (patient_id, sat, datetime.now())
        )

        conn.commit()
        cursor.close()
        conn.close()

        print(f"[{datetime.now()}] T={{temp}}°C  S={{sat}}% – salvate cu succes.")
    except mysql.connector.Error as err:
        print(f"[EROARE MySQL] {{err}}")

def run_simulator():
    while True:
        temp = genereaza_temperatura()
        sat = genereaza_saturatie()
        salveaza_in_baza(temp, sat)
        time.sleep(5)

if __name__ == "__main__":
    run_simulator()
