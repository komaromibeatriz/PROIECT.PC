import mysql.connector
from web3 import Web3
import json
from datetime import datetime

# DataBase
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="parola_ta",
    database="monitorizare"
)

cursor = db.cursor(dictionary=True)
query = """
SELECT 
    p.patient_id, p.value AS pulse, s.value AS saturation, t.value AS temperature, p.timestamp
FROM pulses p
JOIN saturations s ON p.patient_id = s.patient_id AND p.timestamp = s.timestamp
JOIN temperatures t ON p.patient_id = t.patient_id AND p.timestamp = t.timestamp
ORDER BY p.timestamp ASC
"""
cursor.execute(query)
records = cursor.fetchall()

# Connet to Web3 
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
with open("PulseLoggerABI.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address="0x5B38Da6a701c568545dCfcB03FcB875f56beddC4", abi=abi)
account = w3.eth.accounts[0]

# Send to the Blockchain
def log_vitals(pulse, saturation, temperature, patient_id):
    temp_scaled = int(temperature * 100)
    nonce = w3.eth.get_transaction_count(account)
    tx = contract.functions.logVitals(pulse, saturation, temp_scaled, patient_id).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei')
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key="0xPRIVATE_KEY")
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Logat pe Blockchain (pulse={pulse}, saturation={saturation}, temp={temperature}) → TX Hash: {tx_hash.hex()}")

# Send with loop
for row in records:
    log_vitals(row['pulse'], row['saturation'], row['temperature'], row['patient_id'])
 
