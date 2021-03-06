#-*-coding:utf-8-*-
import json
import os
import shutil

#La siguiente función añade una quedada en el chat.

def add_quedada(cid):
    with open('Database/quedadas.json', 'r') as quedadasfile:
        id_quedada_chat = json.load(quedadasfile)
        id_quedada_chat['list_quedadas'].append(cid)

    with open('Database/quedadas.json', 'w') as quedadasfile:
        json.dump(id_quedada_chat, quedadasfile, indent = 2)

    os.mkdir('Database/q/%s' %str(cid))

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        data = {"asistentes" : [], "lugar" : "", "fecha" : "", "hora" : ""}
        json.dump(data, basefile, indent = 2)

# Para eliminar una quedada primero comprobaremos si existe.

def exist_quedada(cid):
    with open('Database/quedadas.json', 'r') as quedadasfile:
        quedadas = json.load(quedadasfile)['list_quedadas']
        if cid in quedadas:
            return True
        else:
            return False

# A continuación, borraremos la quedada.

def delete_quedada(cid):
    with open('Database/quedadas.json', 'r') as quedadasfile:
        quedadas = json.load(quedadasfile)
        for id_quedada_chat in quedadas['list_quedadas']:
            if cid == int(id_quedada_chat):
                quedadas['list_quedadas'].remove(id_quedada_chat)

    with open('Database/quedadas.json', 'w') as quedadasfile:
        json.dump(quedadas, quedadasfile, indent = 2)

    shutil.rmtree('Database/q/%s' %str(cid))
