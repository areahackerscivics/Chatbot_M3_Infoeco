#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pymongo
import logging
from variables import *
from datetime import datetime # Para insertar la fecha actual
import time #Librería con funcionalidades manipular y dar formato a fechas y horas


#from variables import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    urlMongoDB =host #URL_de_MongoDB
    port = port
except Exception as e:
    print (time.strftime("%c"), "- Error al cargar la URL del MongoDB: ", type(e), e)

# urlMongoDB = "mongodb://valenciaApp:valenciaApp@ds127321.mlab.com:27321/datos_valencia"

client = pymongo.MongoClient(urlMongoDB,port)
db = client.prueba  #db = client.get_default_database() # Accedemos a la BD donde tenemos las colecciones
dbUsuarios = db.usuarios
dbMensajes = db.mensajes

#msg['from']={'nombre': 'Arnau', '_id': 192224003, 'idioma': 'cast'}


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insertarNuevoUsuario(idUsario):
    query = {
        '_id': idUsario,
        'idioma': "Cast",
        'fechaInsercion': datetime.now(),
        'fechaUltimoAcceso': datetime.now(),
        'numPreguntas': 1
    }

    try:
        dbUsuarios.insert_one(query)
    except Exception as e:
        logging.exception("- Error al insertar Usuario: ")

def existe_Usuario(idUsuario):
  #### de vueleve true si el usuario exite
  query = {
        '_id': idUsuario
  }
  usuario = dbUsuarios.find_one(query)
  if usuario == 'None':
    return False
  else:
    return True
      

def get_idioma(idUsuario):
  query = {
        '_id': idUsuario
  } 
  try:
    usuario = dbUsuarios.find_one(query)
    idioma = usuario['idioma']

  except Exception as e:
     logging.exception("- Error en buscar Idioma ")
     return 'Cast'
   
  return idioma
  
    
  
def buscarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    try:
        cursor = dbUsuarios.find_one(query)
    except Exception as e:
        #print(time.strftime("%c"), "- Error en buscar Usuario: ", type(e), e)
        logging.exception( "- Error en buscar Usuario: ")
    return cursor

def insertarMensaje(mensaje_user,respuesta_bot):
    
    #fechaUnix = mensaje['date'].now()
    #mensaje['date'] = fechaUnix #datetime.fromtimestamp(fechaUnix)
    mensaje = {
       'date': mensaje_user.date.now().strftime("%Y-%m-%d %H:%M:%S"),
       'idUsuario': mensaje_user.chat.id,
       'texto_usuario': mensaje_user.text,
       'lenguaje':mensaje_user.from_user.language_code,
        'respuesta_bot':respuesta_bot}
    try:
        
        dbMensajes.insert_one(mensaje)
    except Exception as e:
        logging.exception( "- Error en insertar mensaje: ")

def actualizarUsuario(idUsario):
    query = {
        '_id': idUsario
    }
    update = { '$inc': { 'numPreguntas': 1}, '$set': {'fechaUltimoAcceso': datetime.now()}}

    try:
        dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        logging.exception("- Error en Actualizar Usuario:") 


def actualizarIdioma(idUsario,idioma):
    query = {
        '_id': idUsario
    }
    update = {'$set': {'idioma': idioma}}
    try:
        result = dbUsuarios.update_one(query,update)
        return True
    except Exception as e:
        print(time.strftime("%c"), "- Error en actualizar idioma: ", type(e), e)

def actualizarRespuesta(message_id, chat_id, respuesta, accion):
    query = {
        'chat.id': chat_id,
        'message_id': message_id
    }
    update = {'$set': {'respuesta_accion': accion, 'respuesta_texto':respuesta}}
    try:
        dbMensajes.update_one(query,update)
    except Exception as e:
        logging.exception("- Error en Actualizar respuesta: ") 


def addComa(num):
  #need to be string to add coma
  num = str(num)
  try:
     i = num.index('.')
     num = num.replace(num[i], ',')
  except:
     i = len(num)
  
  while i > 3:
     i =i - 3
     num = num[:i] + '.' + num[i:]
  return num



if __name__ == '__main__':
  print(addComa('552222225'))



