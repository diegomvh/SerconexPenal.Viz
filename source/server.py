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
    for habilita in mongo.db.Habilitaciones.find():
        habilitaciones.setdefault(habilita["habilitante"], []).append(habilita["habilitado"])
        habilitaciones.setdefault(habilita["habilitado"], [])
    result = [ {"name": key.split()[-1], "habilitaciones": list(set(value)) } for key, value in habilitaciones.items() ]
    return json.dumps(result)

if __name__ == "__main__":
    app.run()