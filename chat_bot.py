#!/usr/bin/python
# -*- coding: utf-8 -*-
import texto
import ayuntament
import logging 
from apiai import *
from variables import*
from DAO import*
from telegram import  (ReplyKeyboardMarkup, ReplyKeyboardRemove, User, Bot,InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler, Filters,RegexHandler,CallbackQueryHandler)
#filename="chat_bot.log"

'''
Hola usuarix, soy infoecoVLC un chatbot creado con la intención de resolver preguntas acerca de la situación financiera del ayuntamiento de valencia.
Sin embargo necesito que me entrenes para poder hacerlo bien, al principio me va a costar pero ya veras como mejoro con el tiempo. Entrenarme es muy fácil solo tienes que hacerme preguntas y si te apetece, puedes decirme si te he respondido de forma adecuada a tu pregunta Gracias.
'''

logging.basicConfig(filename="chat_bot.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


tecladoIdioma = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Valencià', callback_data='Val'),
     InlineKeyboardButton(text='Castellano', callback_data='Cast')],#Dentro de la lista para que se vea en la misma línea
  ])
  
teclado_respuesta_bot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Sí', callback_data='si'),
     InlineKeyboardButton(text='No', callback_data='no'),
     InlineKeyboardButton(text='NS/NC', callback_data='ns/nc')],#Dentro de la lista para que se vea en la misma línea
  ])

def start(bot,update):
  ### le pasamos la id de telegram para registrar usuario nuevo.
  ## if the user exists we update the last time access to actual time, if not we add the user to the DB
  if existe_Usuario(update.message.chat_id):
    insertarNuevoUsuario(update.message.chat_id)
  else:
    actualizarUsuario(update.message.chat_id)
  leng = get_idioma(update.message.chat_id)

  bot.sendMessage(chat_id = update.message.chat_id, text= texto.respuesta_bot('comandoStart',leng))
  update.message.reply_text('Idioma:', reply_markup=tecladoIdioma)
  
def idioma(bot,update):
  leng = get_idioma(update.message.chat_id)

  bot.sendMessage(chat_id = update.message.chat_id, text= texto.respuesta_bot('comandoIdioma',leng))
  update.message.reply_text('Idioma:', reply_markup=tecladoIdioma)

def button(bot,update):
    ## this function allow the user change the language between spanish and valenciano 
    query = update.callback_query

    if query.data in ['Val','Cast']:
        actualizarIdioma(query.message.chat.id,query.data)
        bot.answerCallbackQuery(callback_query_id= query.id, text=texto.respuesta_bot('pulsarBotonIdioma',query.data))
        bot.sendMessage(chat_id =query.message.chat_id, text=texto.respuesta_bot('respuestaCambioIdioma',query.data))
    if query.data in ['si','no','ns/nc']:
        leng=get_idioma(query.message.chat.id)
        insertar_feedback(query)
        #bot.answerCallbackQuery(callback_query_id= query.id, text=texto.respuesta_bot('feedback',leng))
        bot.edit_message_text(text=texto.respuesta_bot('feedback',leng),
                          chat_id=query.message.chat_id,
                           message_id=query.message.message_id)

def ayuda(bot, update):
   bot.sendMessage(chat_id = update.message.chat.id, text ='puedes preguntarme cualquier cosa sobre la situación financiera yo tratare de responder')
    
def mensaje(bot,update):
   ## if the user send a message to the bot, the program call this function to answer the user question.
   ### query is a function from apiai librery this function manage all the answer.
   if not existe_Usuario(update.message.chat_id):
      insertarNuevoUsuario(update.message.chat_id)
   else:
      actualizarUsuario(update.message.chat_id)
   good , text =query(update.message.text, update.message.chat_id,get_idioma(update.message.chat_id))
   leng=get_idioma(update.message.chat_id)
   bot.sendMessage(chat_id=update.message.chat_id, text=text)
   
   if good:
     update.message.reply_text(respuesta_bot('res.Correcta',leng), reply_markup=teclado_respuesta_bot)
   
   insertarMensaje(update.message,text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

  updater = Updater(Token)

  
  updater.start_polling()
  updater.dispatcher.add_handler(CommandHandler('start',start))
  updater.dispatcher.add_handler(CommandHandler('inicio',start))
  updater.dispatcher.add_handler(CommandHandler('ayuda',ayuda))
  updater.dispatcher.add_handler(CommandHandler('idioma',idioma))
  updater.dispatcher.add_handler(MessageHandler(Filters.text,mensaje))
  updater.dispatcher.add_handler(CallbackQueryHandler(button))
  updater.dispatcher.add_error_handler(error)
  #updater.start_webhook(listen='0.0.0.0',
  #                    port=8443,
  #                    url_path=variables.Token_bot,
  #                    key='private.key',
  #                    cert='cert.pem',
  #                    webhook_url='{}:8443/{}'.format(variables.url, variables.Token_bot))

  updater.idle()

if __name__ == '__main__':
  main()
