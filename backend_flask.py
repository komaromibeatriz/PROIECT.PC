# app.py

from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_latest_pulse():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT p.id AS pulse_id, p.value, p.timestamp, pt.name AS patient_name
    FROM pulses p
    JOIN patients pt ON pt.id = p.patient_id
    ORDER BY p.timestamp DESC
    LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_pulses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT p.id AS pulse_id, p.value, p.timestamp, pt.name AS patient_name
    FROM pulses p
    JOIN patients pt ON pt.id = p.patient_id
    ORDER BY p.timestamp DESC
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.route('/')
def home():
    return "Pulse Monitor API is running."

@app.route('/latest')
def latest():
    pulse = get_latest_pulse()
    return jsonify(pulse)

@app.route('/api/v1/pulse')
def all_pulses():
    pulses = get_all_pulses()
    return jsonify(pulses)

if __name__ == '__main__':
    app.run(debug=True)
