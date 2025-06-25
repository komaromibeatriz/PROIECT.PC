
from flask import Blueprint, jsonify
from plugin_fhir.schemas import generate_fhir_observation

fhir_bp = Blueprint('fhir', __name__, url_prefix='/api/fhir')

@fhir_bp.route('/Observation/<int:obs_id>', methods=['GET'])
def get_observation(obs_id):
    # Exemplu static de date (poate fi modificat pentru integrare cu DB)
    observation = generate_fhir_observation(obs_id, 77, "2025-06-25T12:00:00+03:00", "bpm")
    return jsonify(observation)
