#!/usr/bin/env python

# This is one of the many reasons why python 3 is better than python 2
# Run this script with python2 and then with python3

import sys
import re
import functools
import time
from datetime import datetime

def compose(*functions):
    return functools.reduce(
        lambda f, g: lambda x: f(g(x)), 
        functions, 
        lambda x: x
    )

# Headers
AUDITORIAS = [
    "documento", "localidad", "roles", "ultima_actividad",
    "actividad", "accion", "modelo", "objeto_id", "viejo_estado",
    "nuevo_estado", "momento", "user_agent", "ip", "url", "url_referrer"
]

CAUSAS = [ 
    "habilitado", "causa_id", "tipo", "desde", "hasta", "habilitante",
    "opciones"
]

# Roles
ROLES = {
    "administrador": 1 << 0,
    "defensa": 1 << 1,
    "delegado": 1 << 2,
    "fiscal": 1 << 3,
    "profesional": 1 << 4,
    "usuario": 1 << 5
}

OPCIONES = {
    "otorgable": 1 << 0,
    "completa": 2 << 0    
}

ACCIONES = {
    "C": "Create",
    "R": "Read",
    "U": "Update",
    "D": "Delete",
    "I": "In",
    "O": "Out",
    "E": "Error",
    "L": "Log"
}

RE_DATETIME = re.compile("\d{2,4}-\d{2}-\d{2} \d{2,4}:\d{2,4}:\d{2,4}.\d{3}")
RE_NUMERO = re.compile("^\d+$")
# gephi
# d3
# prefuse
# NetworkX
# Circos
def get_roles(code):
    roles = []
    for key, value in ROLES.items():
        if code and code & value:
            roles.append(key)
    return roles

def map_roles(doc):
    doc["roles"] = get_roles(doc["roles"])
    return doc
    
def map_accion(doc):
    doc["accion"] = ACCIONES[doc["accion"]]
    return doc

def get_opciones(code):
    opciones = []
    for key, value in OPCIONES.items():
        if code and code & value:
            opciones.append(key)
    return opciones

def map_opciones(doc):
    doc["opciones"] = get_opciones(doc["opciones"])
    return doc

def fix_numero(doc):
    for key in doc.keys():
        if type(doc[key]) == str and len(doc[key]) < 6 and RE_NUMERO.match(doc[key]):
            doc[key] = int(doc[key])
    return doc
    
def fix_datetime(doc):
    for key in doc.keys():
        if type(doc[key]) == str and RE_DATETIME.match(doc[key]):
            doc[key] = datetime.strptime(doc[key], "%Y-%m-%d %H:%M:%S.%f")
    return doc
    
def fix_null(doc):
    for key in doc.keys():
        if doc[key] == 'NULL':
            doc[key] = None
    return doc

def parse_linea(headers, linea):
    return {t[0]: t[1] for t in zip(headers, linea.split(','))}

def get_documents(filename, processing):
    with open(filename, "r") as f:
        data = f.read().replace('\r\n','\n').replace('\r','\n')
        return map(processing, data.splitlines())

def show_some_data(iterable, max):
    for i, data in enumerate(iterable):
        print(data)
        if i > max:
            break

def format_data(value):
    return value and "%s" % value or ""

def dump_csv_data(filename, headers, data):
    with open(filename, "w") as f:
        f.writelines([",".join(headers)])
        f.writelines([
            ",".join([format_data(d[key]) for key in headers ])  for d in data ])

def main(args=sys.argv):
    now = time.time()
    auditorias = get_documents("../data/auditoria.csv", compose(
        map_accion, map_roles, fix_null, fix_datetime, fix_numero,
        functools.partial(parse_linea, AUDITORIAS)
    ))
    print("Auditorias", time.time() - now)
    now = time.time()
    causas = get_documents("../data/causas.csv", compose(
        map_opciones, fix_null, fix_datetime, fix_numero,
        functools.partial(parse_linea, CAUSAS)
    ))
    print("Causas", time.time() - now)
    headers = CAUSAS[:]
    headers.remove("opciones")
    dump_csv_data("causas.csv", headers, causas)
    #show_some_data(auditorias, 10)
    #show_some_data(causas, 10)
    return 0    

if __name__ == '__main__':
    sys.exit(main())