# !/usr/bin/env python
# -*- coding:utf-8 -*-
import telebot
import private as tk
from libs import fiestas as f
from libs import quedadas as q
from libs import aux
from libs import lugarfiestas as lf
from libs import lugarquedadas as lq
from libs import fechasfiestas as ff
from libs import fechasquedadas as fq
from libs import AsistentesQuedadas as aq

token = tk.get_token()
bot = telebot.TeleBot(token)


def send(m, text):
    bot.send_message(m.chat.id, text)


@bot.message_handler(commands='cr_party')
def create_party(m):
    cid = m.chat.id
    if f.exist_fiesta(cid):
        send(m, 'Ya hay una fiesta creada')
    else:
        f.add_fiesta(cid)
        send(m, 'Fiesta creada con éxito')


@bot.message_handler(commands='cr_quedada')
def create_quedada(m):
    cid = m.chat.id
    if q.exist_quedada(cid):
        send(m, 'Ya hay una quedada creada')
    else:
        q.add_quedada(cid)
        send(m, 'Quedada creada con éxito')


@bot.message_handler(commands='del_party')
def delete_party(m):
    cid = m.chat.id
    if f.exist_fiesta(cid):
        f.delete_fiesta(cid)
        send(m, 'Fiesta eliminada correctamente')
    else:
        send(m, 'No hay fiesta creada')


@bot.message_handler(commands='del_quedada')
def delete_quedada(m):
    cid = m.chat.id
    if q.exist_quedada(cid):
        q.delete_quedada(cid)
        send(m, 'Quedada eliminada correctamente')
    else:
        send(m, 'No hay quedada creada')


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
