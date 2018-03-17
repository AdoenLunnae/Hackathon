import json

#FUNCIONES PARA LA LISTA DE LA COMPRA
#La siguiente función añade un nuevo item a la lista de la compra.

def add_item_compra(cid, item):
    with open('Database/f/%s/compra.json' %str(cid), 'r') as itemcompra:
        compras = json.load(itemcompra)
        compras['list_compra'][item]= ':x:'
    with open('Database/f/%s/compra.json' %str(cid), 'w') as itemcompra:
        json.dump(compras, itemcompra, indent = 2)

#La siguiente función marca con un tick el item de la compra pasado como argumento.

def check_item_compra(cid, item):
    with open('Database/f/%s/compra.json' %str(cid), 'r') as itemcompra:
        compras = json.load(itemcompra)
        compras['list_compra'][item]= ':heavy_check_mark:'
    with open('Database/f/%s/compra.json' %str(cid), 'w') as itemcompra:
        json.dump(compras, itemcompra, indent = 2)

#La siguiente función elimina un item del diccionario list_compra.

def del_item_compra(cid, item):
    with open('Database/f/%s/compra.json' %str(cid), 'r') as itemcompra:
        compras = json.load(itemcompra)
        compras['list_compra'].remove(item)
    with open('Database/f/%s/compra.json' %str(cid), 'r') as itemcompra:
        json.dump(compras, itemcompra, indent = 2)


#FUNCIONES PARA LAS PETICIONES

#La siguiente función añade una petición de un usuario.

def add_peticion(cid, uid, peticion):
    with open('Database/f/%s/peticiones.json' %str(cid), 'r') as peticionesfile:
        peticiones = json.load(peticionesfile)
        peticiones['list_music'][uid].append(peticion)

    with open('Database/f/%s/peticiones.json' %str(cid), 'r') as peticionesfile:
        json.dump(peticiones, peticionesfile, indent = 2)

#La siguiente función imprime todas las peticiones.

def print_peticiones(cid, uid):
    with open('Database/f/%s/peticiones.json' %str(cid), 'r') as peticionesfile:
        peticiones = json.load(peticionesfile)
        num = 1
        cadena = ''
        for peti_de_u in peticiones['list_music'][uid]:
            cadena += str(num) + ': ' + peti_de_u + '\n'
            num += 1
    return cadena

#La siguiente función borra la petición aportada por el user.

def del_peticion(cid, uid, peticion):
    with open('Database/f/%s/peticiones.json' %str(cid), 'r') as peticionesfile:
        peticiones = json.load(peticionesfile)
        peticiones['list_music'][uid].remove(peticion)

    with open('Database/f/%s/peticiones.json' %str(cid), 'w') as peticionesfile:
        json.dump(peticiones, peticionesfile, indent = 2)
