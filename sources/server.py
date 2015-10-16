#!/usr/bin/env python
import flask
import json
from flask.ext.pymongo import PyMongo

app = flask.Flask(__name__)
app.config["MONGO_DBNAME"] = "SerconexPenal"
mongo = PyMongo(app)

@app.route("/tree")
def tree():
    return flask.render_template('tree.html')

@app.route("/habilitaciones")
def habilitaciones():
    return flask.render_template('habilitaciones.html')

@app.route("/habilitaciones.json")
def habilitaciones_json():
    habilitaciones = {}
    roles = { "Trelew": [ "oficina" ] }
    for habilita in mongo.db.Habilitaciones.find():
        habilitaciones.setdefault(habilita["habilitante"], []).append(habilita["habilitado"])
        habilitaciones.setdefault(habilita["habilitado"], [])
        roles.setdefault(habilita["habilitante"], habilita.get("roles", []))
    result = [ {
        "name": key, 
        "habilitaciones": list(set(value)),
        "roles": roles.get(key, [])
        } for key, value in habilitaciones.items() ]
    return json.dumps(result)

@app.route("/tree.json")
def tree_json():
    tree = { "name": "root", 
        "children": [
            { "name": "usuario", "children": [
                { "name": "fiscal", "children": [
                  { "name": "profesional", "children": []},
                  { "name": "delegado", "children": []},
                  { "name": "administrador", "children": []},      
                ]},
                { "name": "defensa", "children": [
                  { "name": "profesional", "children": []},
                  { "name": "delegado", "children": []},
                  { "name": "administrador", "children": []},      
                ]},
                { "name": "profesional", "children": []},
                { "name": "delegado", "children": []},
                { "name": "administrador", "children": []},
             ]},
            { "name": "oficina", "children": []},
      ]}
    return json.dumps(tree)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
