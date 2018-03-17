import json

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

#La siguiente función borra la petición aportada por el user.

def del_peticion(cid, uid, peticion):
    with open('Database/f/%s/peticiones.json' %str(cid), 'r') as peticionesfile:
        peticiones = json.load(peticionesfile)
        peticiones['list_music'][uid].remove(peticion)

    with open('Database/f/%s/peticiones.json' %str(cid), 'w') as peticionesfile:
        json.dump(peticiones, peticionesfile, indent = 2)
