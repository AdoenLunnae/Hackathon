import json
import os
import shutil

def add_lugar(cid, lugar):
    with open('Database/f/%s/base.json', %str(cid), 'r') as lugarfiestafile:
        base = json.load(lugarfiestafile)
        base['lugar'].append(lugar)


    with open('Database/f/%s/base.json', %str(cid), 'w') as lugarfiestafile:
        json.dump(base, lugarfiestafile, indent= 2)
