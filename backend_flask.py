from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Generic function to fetch latest value from a table (e.g., pulses, temperatures, saturations)
def get_latest_measurement(table_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
    SELECT t.id AS record_id, t.value, t.timestamp, pt.name AS patient_name
    FROM {table_name} t
    JOIN patients pt ON pt.id = t.patient_id
    ORDER BY t.timestamp DESC
    LIMIT 1
    """

    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Generic function to fetch all records from a table
def get_all_measurements(table_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
    SELECT t.id AS record_id, t.value, t.timestamp, pt.name AS patient_name
    FROM {table_name} t
    JOIN patients pt ON pt.id = t.patient_id
    ORDER BY t.timestamp DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.route('/')
def home():
    return "Health Monitor API is running."

# -------- PULSE ENDPOINTS --------
@app.route('/latest/pulse')
def latest_pulse():
    return jsonify(get_latest_measurement('pulses'))

@app.route('/api/v1/pulse')
def all_pulses():
    return jsonify(get_all_measurements('pulses'))

# -------- TEMPERATURE ENDPOINTS --------
@app.route('/latest/temperature')
def latest_temperature():
    return jsonify(get_latest_measurement('temperatures'))

@app.route('/api/v1/temperature')
def all_temperatures():
    return jsonify(get_all_measurements('temperatures'))

# -------- SATURATION ENDPOINTS --------
@app.route('/latest/saturation')
def latest_saturation():
    return jsonify(get_latest_measurement('saturations'))

@app.route('/api/v1/saturation')
def all_saturations():
    return jsonify(get_all_measurements('saturations'))

if __name__ == '__main__':
    app.run(debug=True)
