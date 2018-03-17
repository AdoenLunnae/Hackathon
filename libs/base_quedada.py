#-*-coding:utf-8-*-
import json

# La siguiente función añade asistentes a la quedada.

def add_asistente_quedada(cid, uname):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        base['asistentes'].append(uname)

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)

# La siguiente función comprueba que existe un asistente para eliminarlo o no más tarde.

def exist_asistente_quedada(cid, uname):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        for userid in base['asistentes']:
            if userid == uname:
                return True
        else:
            return False

def delete_asistente_quedada(cid, uname):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        base['asistentes'].remove(uname)

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)


# La siguiente función establece el lugar de la quedada.

def add_lugar(cid, lugar):
    with open('Database/q/%s/base.json' %str(cid), 'r') as lugarquedadafile:
        base = json.load(lugarquedadafile)
        base['lugar'].append(lugar)


    with open('Database/q/%s/base.json' %str(cid), 'w') as lugarquedadafile:
        json.dump(base, lugarquedadafile, indent= 2)


#La siguiente función establece la fecha de la quedada.

def add_fecha(cid, fecha):
    with open('Database/q/%s/base.json' %str(cid), 'r') as fechaquedadafile:
        base = json.load(fechaquedadafile)
        base['fecha'].append(fecha)


    with open('Database/q/%s/base.json' %str(cid), 'w') as fechaquedadafile:
        json.dump(base, fechaquedadafile, indent= 2)

#La siguiente función establece la hora de la quedada.

def add_hora(cid, hora):
    with open('Database/q/%s/base.json' %str(cid), 'r') as horaquedadafile:
        base = json.load(horaquedadafile)
        base['hora'].append(hora)

    with open('Database/q/%s/base.json' %str(cid), 'w') as horaquedadafile:
        json.dump(base, horaquedadafile, indent = 2)
