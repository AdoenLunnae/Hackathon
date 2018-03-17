# -*-coding:utf-8 -*-
import json

# Está función añade un asistente a la fiesta.

def add_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        base['asistentes'].append(uname)

    with open('Database/f/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)

# Las siguiente función comprueba si existe un asistente para después eliminarlo o no.

def exist_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        for userid in base['asistentes']:
            if userid == uname:
                return True
        else:
            return False

def delete_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        base['asistentes'].remove(uname)

    with open('Database/f/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)


# La siguiente función establece el lugar de la fiesta.

def add_lugar(cid, lugar):
    with open('Database/f/%s/base.json' %str(cid), 'r') as lugarfiestafile:
        base = json.load(lugarfiestafile)
        base['lugar']=lugar


    with open('Database/f/%s/base.json' %str(cid), 'w') as lugarfiestafile:
        json.dump(base, lugarfiestafile, indent= 2)


# La siguiente función establece la fecha de la fiesta.

def add_fecha(cid, fecha):
    with open('Database/f/%s/base.json' % str(cid), 'r') as fechafiestafile:
        base = json.load(fechafiestafile)
        base['fecha']=fecha


    with open('Database/f/%s/base.json' %str(cid), 'w') as fechafiestafile:
        json.dump(base, fechafiestafile, indent= 2)
