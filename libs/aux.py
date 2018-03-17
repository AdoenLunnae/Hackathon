# !/usr/bin/env python
# -*- coding:utf-8 -*-
import json

def is_date(date):
    lst = date.split('/')
    if lst.len() == 2:
        if lst[0].len <= 2 & lst[1].len <= 2:
            return lst[0].isdigit() & lst[1].isdigit()


def get_arg(message):
    lst = message.split(' ')
    if len(lst) == 2:
        return lst[1]


def get_arg2(message):
    lst=message.split(' ')
    if len(lst)==3:
        return lst[1], lst[2]


def get_info(cid, type):
    if type == 'fiesta':
        with open('Database/f/%s/base.json' %str(cid), 'r') as file:
            base=json.load(file)
            asist=base['asistentes']
            asiststr=asist.join(', ')
            fecha=base['fecha']
            lugar=base['lugar']
            return 'La fiesta es el {} en {}. Van {}.'.format(fecha, lugar, asiststr)

    elif type == 'quedada':
        with open('Database/q/%s/base.json' %str(cid), 'r') as file:
            base = json.load(file)
            asist = base['asistentes']
            asiststr = asist.join(', ')
            fecha = base['fecha']
            hora = base['hora']
            lugar = base['lugar']
            return 'La quedada es el {} a las {} en {}. Van {}.'.format(fecha, hora, lugar, asiststr)
    else:
        pass


def is_time(time):
    lst = time.split(':')
    if lst.len() == 2:
        if lst[0].len <= 2 & lst[1].len <= 2:
            return lst[0].isdigit() & lst[1].isdigit()