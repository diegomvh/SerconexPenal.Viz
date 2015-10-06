#!/usr/bin/env python
import flask
import json
from flask.ext.pymongo import PyMongo

app = flask.Flask(__name__)
app.config["MONGO_DBNAME"] = "SerconexPenal"
mongo = PyMongo(app)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/habilitaciones.json")
def habilitaciones():
    habilitaciones = {}
    roles = { "Oficina Judicial de Trelew": ["oficina"] }
    for habilita in mongo.db.Habilitaciones.find():
        habilitaciones.setdefault(habilita["habilitante"], []).append(habilita["habilitado"])
        habilitaciones.setdefault(habilita["habilitado"], [])
        roles.setdefault(habilita["habilitante"], habilita.get("roles", []))
    result = [ {
        "name": key.split()[-1], 
        "habilitaciones": list(set(value)),
        "roles": roles.get(key, [])
        } for key, value in habilitaciones.items() ]
    return json.dumps(result)

if __name__ == "__main__":
    app.run()