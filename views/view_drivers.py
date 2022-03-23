from flask import request, Flask
from models import drivers

app = Flask(__name__)

@app.route("/dr/<id>", methods=["GET"])








