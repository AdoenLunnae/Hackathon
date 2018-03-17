import json
import os
import shutil

#Para borrar una fiesta primero debemos comprobar si existe una fiesta creada en el chat.

def exist_fiesta(cid):
    with open('Database/fiestas.json', 'r') as jsonfile:
        fiestas = json.load(jsonfile)['list_fiestas']
        if cid in fiestas:
                    return True
        else:
                    return False

#Si existe la fiesta, la borraremos.

def delete_fiesta(cid):
    with open('Database/fiestas.json', 'r') as fiestasfile:
        fiestas = json.load(fiestasfile)

        for id_fiesta_chat in fiestas['list_fiestas']:
            if cid == int(fiesta.id):
                fiestas['list_fiestas'].remove(id_fiesta_chat)

#Sobreescribimos el diccionario.

    with open('Database/fiestas.py', 'w') as fiestasfile:
        json.dump(fiestas, fiestasfile)

#Borramos la carpeta creada al crear una fiesta, con sus archivos.

    shutil.rmtree('Database/f/%s' %str(cid))




