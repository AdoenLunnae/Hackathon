# !/usr/bin/env python
# -*- coding:utf-8 -*-
import telebot
import private as tk

token = tk.get_token()
bot = telebot.TeleBot(token)

bot.polling()
