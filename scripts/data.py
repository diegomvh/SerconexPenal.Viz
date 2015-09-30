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
# Cambiar "Error de login," y "Fuera de tiempo," tiene un coma y es mi separador de lineas

if __name__ == '__main__':
    auditorias_docs = []
    with open("auditoria.csv", "r") as f:
        for linea in f.read().splitlines(False):
            tokens = linea.split(',')
            if "Requerimiento" in linea:
                doc = { "documento": tokens[0], "localidad": tokens[1],
                    "roles": tokens[2], "ultima_actividad": tokens[3],
                    "actividad": tokens[4], "accion": tokens[5], 
                    "modelo": tokens[6], "objeto_id": tokens[7], 
                    "viejo_estado": tokens[8], "nuevo_estado": ",".join(tokens[9:-5]),
                    "momento": tokens[-5], "user_agent": tokens[-4], 
                    "ip": tokens[-3], "url": tokens[-2], "url_referrer": tokens[-1] 
                    }
            elif "MensajeLog" in linea:
                doc = { "documento": tokens[0], "localidad": tokens[1],
                    "roles": tokens[2], "ultima_actividad": tokens[3],
                    "actividad": tokens[4], "accion": tokens[5], 
                    "modelo": tokens[6], "objeto_id": tokens[7], 
                    "viejo_estado": tokens[8], "nuevo_estado": ",".join(tokens[9:-6]),
                    "momento": tokens[-5], "user_agent": tokens[-4], 
                    "ip": tokens[-3], "url": tokens[-2], "url_referrer": tokens[-1] 
                }
            else:
                doc = {t[0]: t[1] for t in zip(auditorias, tokens)}
            print(linea, doc)
            doc["momento"] = datetime.strptime(doc["momento"], "%Y-%m-%d %H:%M:%S.%f")
            auditorias_docs.append(doc)
        print(auditorias_docs) 
    with open("causas.csv", "r") as f:
        docs = [ {t[0]: t[1] for t in zip(causas, linea.split(','))} \
            for linea in f.read().splitlines(False) ]
        print(len(docs))

            