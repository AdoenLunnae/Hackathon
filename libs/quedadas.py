import json
import os
import shutil

def add_quedada(cid):
    with open('Database/quedadas.json', 'r') as quedadasfile:
        id_quedada_chat = json.load(quedadasfile)
        id_quedada_chat['list_quedadas'].append(cid)

    with open('Database/quedadas.json', 'w') as quedadasfile:
        json.dump(id_quedada_chat, quedadasfile)

    os.mkdir('Database/q/%s' %str(cid))

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        data = {"asistentes" : [], "lugar" : "", "fecha" : ""}
        json.dump(data, basefile)
