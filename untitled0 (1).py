# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PVLp2hEvZ_Q3dAIvFo_3-FckAPQFhMDv
"""

!pip install pyTelegramBotAPI

import telebot

# جایگزین کن با توکن واقعی خودت
TOKEN = '8086078959:AAEqSNAZ_Hv5_6lwU79DkdEuk1S3zcWH6wc'

bot = telebot.TeleBot(TOKEN)

# حذف webhook
bot.remove_webhook()
print("Webhook removed successfully.")

import telebot
from telebot import types

bot = telebot.TeleBot( '8086078959:AAEqSNAZ_Hv5_6lwU79DkdEuk1S3zcWH6wc' )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "  سلام به ربات خدماتی خوش اومدی برای عضویت روی گزینه ی   /membership کلیک کن")

if __name__ == '__main__':
    bot.polling()