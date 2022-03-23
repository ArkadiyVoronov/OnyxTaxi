from models.clients import clients
from flask import request, jsonify
#from model import db

@app.route("/clients/<id>", methods=["GET"])
def get_clients():
    cli = clients

@app.route("/clients/", methods=["POST"])
def create_clients():

    body = request.get_json()
    # TODO: vlidate body
    new_cli = clients(**body)
    
    db.session.add(new_cli)
    db.session.commit()