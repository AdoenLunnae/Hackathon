import json
import os
import shutil

def add_fiesta(cid):
    with open('Database/fiestas.json', 'r') as fiestasfile:
        id_fiesta_chat = json.load(fiestasfile)
        id_fiesta_chat['list_fiestas'].append(cid)

    with open('Database/fiestas.json', 'w') as fiestasfile:
        json.dump(id_fiesta_chat, fiestasfile, indent = 2)

    os.mkdir('Database/f/%s' %str(cid))

    with open('Database/f/%s/base.json' %str(cid), 'w') as basefile:
        data = {"asistentes" : [], "lugar" : "", "fecha" : ""}
        json.dump(data, basefile, indent = 2)

    with open('Database/f/%s/compra.json' %str(cid) 'w') as comprasfile
        data = {"list_compra" : {}}



#Para borrar una fiesta primero debemos comprobar si existe una fiesta creada en el chat.

def exist_fiesta(cid):
    with open('Database/fiestas.json', 'r') as fiestasfile:
        fiestas = json.load(fiestasfile)['list_fiestas']
        if cid in fiestas:
            return True
        else:
            return False

#Si existe la fiesta, la borraremos.

def delete_fiesta(cid):
    with open('Database/fiestas.json', 'r') as fiestasfile:
        fiestas = json.load(fiestasfile)

        for id_fiesta_chat in fiestas['list_fiestas']:
            if cid == int(id_fiesta_chat):
                fiestas['list_fiestas'].remove(id_fiesta_chat)

#Sobreescribimos el diccionario.

    with open('Database/fiestas.json', 'w') as fiestasfile:
        json.dump(fiestas, fiestasfile, indent = 2)

#Borramos la carpeta creada al crear una fiesta, con sus archivos.

    shutil.rmtree('Database/f/%s' %str(cid))
