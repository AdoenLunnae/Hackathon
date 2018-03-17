# !/usr/bin/env python
# -*- coding:utf-8 -*-
import telebot
import private as tk
from libs import fiestas as f
from libs import quedadas as q
from libs import aux
from libs import base_quedada as bq
from libs import base_fiesta as bf
from libs import extras_fiesta as ef

token = tk.token
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
            send(m, 'Quedada eliminada correctamente')
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
    cid=m.chat.id
    if (arg == 'fiesta') or (arg=='quedada'):
        send(m, aux.get_info(cid, arg))
    else:
        send(m, 'Usa /info + "fiesta" o "quedada"')

@bot.message_handler(commands='date')
def date(m):
    cid = m.chat.id
    type, date=aux.get_arg2(m.text)
    if aux.is_date(date):
        if type=='fiesta':
            if f.exist_fiesta(cid):
                bf.add_fecha(cid, date)
            else:
                send('La fiesta no está creada')
        elif type=='quedada':
            if q.exist_quedada(cid):
                bq.add_fecha(cid, date)
            else:
                send(m, 'La quedada no existe')
    else:
        send(m, 'Usa /date + "fiesta" o "quedada" + fecha(DD/MM)')

@bot.message_handler(commands= 'place' )
def place(m):
    cid = m.chat.id
    type, date = aux.get_arg2(m.text)
    if type == 'fiesta':
        if f.exist_fiesta(cid):
            bf.add_lugar(cid, date)
        else:
            send('La fiesta no está creada')
    elif type == 'quedada':
        if q.exist_quedada(cid):
            bq.add_lugar(cid, date)
        else:
            send(m, 'La quedada no existe')
    else:
        send(m, 'Usa /date + "fiesta" o "quedada" + lugar')

@bot.message_handler(commands= 'time')
def time(m):
    cid=m.chat.id
    time=aux.get_arg(m.text)
    if aux.is_time(time):
        if q.exist_quedada(cid):
            bq.add_hora(cid, time)
        else:
            send(m, 'La quedada no existe')
    else:
        send(m, 'Usa /time + hora(HH:MM)')


@bot.message_handler(commands='lista')
def lista(m):
    cid=m.chat.cid
    action, item=aux.get_arg2(m.text)
    if action=='add':
        if f.exist_fiesta(cid):
            ef.add_item_compra(cid, item)
        else:
            send(m, 'La fiesta no existe')
    elif action=='mark':
        if f.exist_fiesta(cid):
            ef.check_item_compra(cid, item)
        else:
            send(m, 'La fiesta no existe')
    elif action == 'remove':
        if f.exist_fiesta(cid):
            ef.del_item_compra(cid, item)
        else:
            send(m, 'La fiesta no existe')
    else:
        send(m, 'Usa /lista + "add"/"mark"/"remove" + item')

@bot.message_handler(commands='music')
def musica(m):
    cid = m.chat.cid
    action, item = aux.get_arg2(m.text)
    uid= m.from_user.uid
    if action == 'add':
        if f.exist_fiesta(cid):
            ef.add_peticion(cid, item)
        else:
            send(m, 'La fiesta no existe')
    elif action == 'view':
        if f.exist_fiesta(cid):
            ef.print_peticiones(cid, uid)
        else:
            send(m, 'La fiesta no existe')
    elif action == 'remove':
        if f.exist_fiesta(cid):
            ef.del_peticion(cid, item)
        else:
            send(m, 'La fiesta no existe')
    else:
        send(m, 'Usa /lista + "add"+titulo/"view"/"remove"+posicion ')



bot.polling()
