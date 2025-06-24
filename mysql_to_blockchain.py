 import mysql.connector
from web3 import Web3
import json

# 1. Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="parola_ta",       # ← write your own password here
    database="monitorizare"
)

cursor = db.cursor()
cursor.execute("SELECT value FROM pulses ORDER BY timestamp ASC")
pulse_values = [row[0] for row in cursor.fetchall()]

# 2.Connect to Web3 (Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Connect to Ganache 
with open("PulseLoggerABI.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address="0xContractAddress", abi=abi)  # ←Write your contract address
account = w3.eth.accounts[0]

# 3. Save Pulse value to Blockchain
def log_pulse(value):
    nonce = w3.eth.get_transaction_count(account)
    tx = contract.functions.logPulse(value).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.to_wei('10', 'gwei')
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key="0xPRIVATE_KEY")  # 
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Pulse {value} loglandı → TX Hash: {tx_hash.hex()}")

# 4. Send all pulse data
for pulse in pulse_values:
    log_pulse(pulse)
