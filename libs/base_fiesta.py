import json

#FUNCIONES PARA AÑADIR Y ELMINAR ASISTENTES DE UNA FIESTA

def add_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        base['asistentes'].append(uname)

    with open('Database/f/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)

def exist_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        for userid in base['asistentes']:
            if userid == uname: return True
        else: False

def delete_asistente_fiesta(cid, uname):
    with open('Database/f/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        base['asistentes'].remove(uname)

    with open('Database/f/%s/base.json' %str(cid), 'w') as basefile:
        jason.dump(base, basefile, indent = 2)


#FUNCION PARA ESTABLECER LUGAR FIESTA

def add_lugar(cid, lugar):
    with open('Database/f/%s/base.json' %str(cid), 'r') as lugarfiestafile:
        base = json.load(lugarfiestafile)
        base['lugar'].append(lugar)


    with open('Database/f/%s/base.json' %str(cid), 'w') as lugarfiestafile:
        json.dump(base, lugarfiestafile, indent= 2)


#FUNCION PARA ESTABLECER FECHA FIESTA

def add_fecha(cid, fecha):
    with open('Database/f/%s/base.json' % str(cid), 'r') as fechafiestafile:
        base = json.load(fechafiestafile)
        base['fecha'].append(fecha)


    with open('Database/f/%s/base.json' %str(cid), 'w') as fechafiestafile:
        json.dump(base, fechafiestafile, indent= 2)
