from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import settings

from hack_tool import clinic_blueprint

app = Flask(__name__)
app.register_blueprint(clinic_blueprint)



CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6001)
