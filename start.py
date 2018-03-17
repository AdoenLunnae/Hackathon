# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json

os.mkdir('Database')
os.mkdir('Database/q')
os.mkdir('Database/f')
with open('Database/quedadas.json', 'w') as f:
    data = {'list_quedadas': []}
    json.dump(data, f, indent = 2)
with open('Database/fiestas.json', 'w') as f:
    data = {'list_fiestas': []}
    json.dump(data, f, indent = 2)
