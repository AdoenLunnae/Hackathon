import json
import os
import shutil

def add_lugar(cid, lugar):
    with open('Database/q/%s/base.json' %str(cid), 'r') as lugarquedadafile:
        base = json.load(lugarquedadafile)
        base['lugar'].append(lugar)


    with open('Database/q/%s/base.json' %str(cid), 'w') as lugarquedadafile:
        json.dump(base, lugarquedadafile, indent= 2)
