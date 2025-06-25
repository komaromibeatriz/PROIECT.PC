
from flask import Flask
from plugin_fhir.api.routes import fhir_bp

app = Flask(__name__)
app.register_blueprint(fhir_bp)

if __name__ == "__main__":
    app.run(debug=True)
