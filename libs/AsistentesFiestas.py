def add_asistente_fiestas(cid, uid):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        base['asistentes'].append(uid)

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        json.dump(base, basefile, indent = 2)

def exist_asistente_fiestas(cid, uid):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        for userid in base['asistentes']:
            if userid == uid: return True
        else: False

def delete_asistente_fiestas(cid, uid):
    with open('Database/q/%s/base.json' %str(cid), 'r') as basefile:
        base = load.json(basefile)
        base['asistentes'].remove(uid)

    with open('Database/q/%s/base.json' %str(cid), 'w') as basefile:
        jason.dump(base, basefile, indent = 2)
