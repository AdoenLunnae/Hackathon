import json
import os
import shutil

def add_fecha(cid, fecha):
    with open('Database/q/%s/base.json' %str(cid), 'r') as fechaquedadafile:
        base = json.load(fechaquedadafile)
        base['fecha'].append(fecha)


    with open('Database/q/%s/base.json' %str(cid), 'w') as fechaquedadafile:
        json.dump(base, fechaquedadafile, indent= 2)
