# !/usr/bin/env python
# -*- coding:utf-8 -*-
import telebot
import private as tk
from libs import fiestas as f
from libs import quedadas as q


token = tk.get_token()
bot = telebot.TeleBot(token)


def send(m, text):
    bot.send_message(m.chat.id, text)


@bot.message_handler(commands='cr_party')
def create_party(m):
    cid = m.chat.id
    if f.exist_fiesta(cid):
        send(cid, 'Ya hay una fiesta creada')
    else:
        f.add_fiesta(cid)
        send(cid, 'Fiesta creada con éxito')


@bot.message_handler(commands='cr_quedada')
def create_quedada(m):
    cid = m.chat.id
    if q.exist_quedada(cid):
        send(cid, 'Ya hay una fiesta creada')
    else:
        q.add_quedada(cid)
        send(cid, 'Fiesta creada con éxito')


@bot.message_handler(commands='del_party')
def delete_party(m):
    cid = m.chat.id
    if f.exist_fiesta(cid):
        f.delete_fiesta(cid)
        send(cid, 'Fiesta eliminada correctamente')
    else:
        send(cid, 'No hay fiesta creada')


@bot.message_handler(commands='del_quedada')
def delete_quedada(m):
    cid = m.chat.id
    if q.exist_quedada(cid):
        q.delete_quedada(cid)
        send(cid, 'Quedada eliminada correctamente')
    else:
        send(cid, 'No hay quedada creada')


bot.polling()
