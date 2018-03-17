import json
import os
import shutil

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
