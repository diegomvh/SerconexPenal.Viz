#!/usr/bin/env python
from datetime import datetime

auditorias = [ "documento", "localidad", "roles", "ultima_actividad",
    "actividad", "accion", "modelo", "objeto_id", "viejo_estado",
    "nuevo_estado", "momento", "user_agent", "ip", "url", "url_referrer" ]
causas = [ "habilitado", "causa_id", "tipo", "desde", "hasta", "habilitante",
    "opciones"]

# gephi
# d3
# prefuse
# NetworkX
# Circos
if __name__ == '__main__':
    with open("../data/auditoria.csv", "r") as f:
        docs = [ {t[0]: t[1] for t in zip(auditorias, linea.split(','))} \
            for linea in f.read().splitlines(False) ]
        print(len(docs))
    with open("../data/causas.csv", "r") as f:
        docs = [ {t[0]: t[1] for t in zip(causas, linea.split(','))} \
            for linea in f.read().splitlines(False) ]
        print(len(docs))

            