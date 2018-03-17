# !/usr/bin/env python
# -*- coding:utf-8 -*-
import telebot
import private as tk
from libs import fiestas as f
from libs import quedadas as q
from libs import aux
from libs import base_quedada as bq
from libs import base_fiesta as bf

token = tk.get_token()
bot = telebot.TeleBot(token)


def send(m, text):
    bot.send_message(m.chat.id, text)


@bot.message_handler(commands='create')
def create(m):
    arg = aux.get_arg(m.text)
    cid = m.chat.id
    if arg == 'fiesta':
        cid = m.chat.id
        if f.exist_fiesta(cid):
            send(m, 'Ya hay una fiesta creada')
        else:
            f.add_fiesta(cid)
            send(m, 'Fiesta creada con éxito')
    elif arg == 'quedada':
        if q.exist_quedada(cid):
            send(m, 'Ya hay una quedada creada')
        else:
            q.add_quedada(cid)
            send(m, 'Quedada creada con éxito')
    else:
        send(m, 'Usa /create + "fiesta" o "quedada"')


@bot.message_handler(commands='del_party')
def delete(m):
    arg = aux.get_arg(m.text)
    cid = m.chat.id
    if arg == 'fiesta':
        if f.exist_fiesta(cid):
            f.delete_fiesta(cid)
            send(m, 'Fiesta eliminada correctamente')
        else:
            send(m, 'No hay fiesta creada')
    elif arg == 'quedada':
        if q.exist_quedada(cid):
            q.delete_quedada(cid)
            send(m, 'Quedada eliminada correctamente')
    else:
        send(m, 'No hay quedada creada')


@bot.message_handler(commands='join')
def join(m):
    cid = m.chat.id
    uname = m.from_user.username
    arg = aux.get_arg(m.text)
    if arg == 'fiesta':
        if bf.exist_asistente_fiesta(cid, uname):
            send(m, 'Ya te habías unido a la fiesta')
        else:
            bf.add_asistente_fiesta(cid, uname)
            send(m, uname+' se ha unido a la fiesta')
    elif arg == 'quedada':
        if bq.exist_asistente_quedada(cid, uname):
            send(m, 'Ya te habías unido a la quedada')
        else:
            bq.add_asistente_quedada(cid, uname)
            send(m, uname+' se ha unido a la fiesta')
    else:
        send(m, 'Usa /join + "fiesta" o "quedada"')


@bot.message_handler(commands='leave')
def leave(m):
    arg = aux.get_arg(m.text)
    uname = m.from_user.username
    cid = m.chat.id
    if arg == 'fiesta':
        if bf.exist_asistente_fiesta(cid, uname):
            bf.delete_asistente_fiesta(cid, uname)
            send(m, uname+ ' ha dejado la fiesta')
        else:
            send(m, 'No te habías unido a la fiesta')
    elif arg == 'quedada':
        if bq.exist_asistente_quedada(cid, uname):
            bq.delete_asistente_quedada(cid, uname)
            send(m, uname+ ' ha dejado la quedada')
        else:
            send(m, 'No te habías unido a la quedada')
    else:
        send(m, 'Usa /leave + "fiesta" o "quedada"')

@bot.message_handler(commands='info')
def info(m):
    arg = aux.get_arg(m.text)
    if arg == 'fiesta':
        pass
    elif arg == 'quedada':
        pass
    else:
        send(m, 'Usa /info + "fiesta" o "quedada"')

bot.polling()
