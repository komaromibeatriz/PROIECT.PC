
# Plugin REST + FHIR (Membrul 5)

Acest modul oferă un endpoint REST compatibil cu FHIR pentru a accesa date despre puls.

## Endpointuri

- `GET /api/fhir/Observation/<id>` — returnează observația FHIR cu un ID dat (simulată static).

## Exemple

```bash
curl http://localhost:5000/api/fhir/Observation/1
```

## Cum se rulează

```bash
pip install flask
python plugin_fhir/app.py
```

## Structură

- `app.py`: aplicația Flask principală
- `api/routes.py`: definește rutele REST
- `schemas.py`: generează structura FHIR
