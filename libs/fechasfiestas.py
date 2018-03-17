import json
import os
import shutil

def add_fecha(cid, fecha):
    with open('Database/f/%s/base.json' % str(cid), 'r') as fechafiestafile:
        base = json.load(fechafiestafile)
        base['fecha'].append(fecha)


    with open('Database/f/%s/base.json' %str(cid), 'w') as fechafiestafile:
        json.dump(base, fechafiestafile, indent= 2)
