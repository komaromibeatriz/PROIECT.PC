
def generate_fhir_observation(obs_id, value, timestamp, unit):
    return {
        "resourceType": "Observation",
        "id": str(obs_id),
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": "8867-4",
                "display": "Heart rate"
            }],
            "text": "Heart rate"
        },
        "effectiveDateTime": timestamp,
        "valueQuantity": {
            "value": value,
            "unit": unit,
            "system": "http://unitsofmeasure.org",
            "code": unit
        }
    }
