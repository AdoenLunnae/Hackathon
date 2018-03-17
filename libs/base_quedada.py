#-*-coding:utf-8-*-
import json

# FUNCIONES PARA AÑADIR Y ELIMINAR AISTENTES DE UNA QUEDADA

def add_asistente_quedada(cid, uname):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = json.load(basefile)
        base['asistentes'].append(uname)

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)

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


#FUNCION ESTABLECER LUGAR QUEDADA

def add_lugar(cid, lugar):
    with open('Database/q/%s/base.json' %str(cid), 'r') as lugarquedadafile:
        base = json.load(lugarquedadafile)
        base['lugar'].append(lugar)


    with open('Database/q/%s/base.json' %str(cid), 'w') as lugarquedadafile:
        json.dump(base, lugarquedadafile, indent= 2)


#FUNCION ESTABLECER FECHA QUEDADA

def add_fecha(cid, fecha):
    with open('Database/q/%s/base.json' %str(cid), 'r') as fechaquedadafile:
        base = json.load(fechaquedadafile)
        base['fecha'].append(fecha)


    with open('Database/q/%s/base.json' %str(cid), 'w') as fechaquedadafile:
        json.dump(base, fechaquedadafile, indent= 2)

#FUNCIÓN ESTABLECER HORA QUEDADA

def add_hora(cid, hora):
    with open('Database/q/%s/base.json' %str(cid), 'r') as horaquedadafile:
        base = json.load(horaquedadafile)
        base['hora'].append(hora)

    with open('Database/q/%s/base.json' %str(cid), 'w') as horaquedadafile:
        json.dump(base, horaquedadafile, indent = 2)        
