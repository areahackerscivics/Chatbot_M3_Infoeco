#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json
import logging

from Salarios import *
from texto import *
from ayuntament import *
from variables import *
from impuesto_barrio import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    apiAccess = apiaccess
    apiDeveloperAccess = apiDeveloperaccess

except Exception as e:
    logging.exception("- Error al cargar tokens de api.ai: ")

#baseURL = "https://api.api.ai/v1/"
baseURL = "https://api.dialogflow.com/v1/"
#baseURL = "https://api.dialogflow.com/v1/query?v=20150910&query=hola&lang=es&sessionId=500737046&timezone=Europe/Madrid"
#v = 20170605 # fecha en formato AAAAMMDD
#v = 20170712 intent
v = 20150910 #one click integration
APIAI_LANG = "es"

headers = {
    'Authorization': 'Bearer '+ apiAccess,
    "Content-Type":"application/json; charset=utf-8"
    }


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sendQuery(texto, chat_id, idioma):
    ### send post to Dialog flow V1 with the user menssage
    contexto = [{
        "name": "usuario",
        "parameters": { "idioma": idioma},
        "lifespan": 1
        }]
    payload = {
        "query": texto,
        "v": v,
        "sessionId": chat_id,
        "contexts": contexto,
        "lang": APIAI_LANG
        }

    url = baseURL+"query"
    try:
      r = requests.post(url, data=json.dumps(payload), headers=headers)
    except Exception as e: 
      logging.exception("error in post request ro dialogflow V1")
    return r

def query(mensaje,idUser, leng):
  res = sendQuery(mensaje,idUser, leng)
  #print(res)
  if res.status_code == 200:
    #if we get a answer from Dialogflow, and get the intent to select the answer that we want
    res = res.json()
    #['result']['resolvedQuery'])
    intent = res['result']['metadata']['intentName']
    if intent == 'Presupuesto':
       #geo , date, presu = res['result']['parameters'].items()
       
       #return presupuesto_general(geo[1], date[1],leng)
       return res['result']['speech']
    if intent == 'Welcome':
       return respuesta_bot(res['result']['action'], leng)

    if intent in ['Default Fallback Intent','Despedida','bot','comiat']:
       return res['result']['speech']

    if intent == 'salario':
       nombre,cargo = res['result']['parameters'].items()
       key = res['result']['action']
       #print(nombre,cargo)
       if nombre[1] !="":
         return salarios(nombre[1],key, leng)
       elif cargo[1] !="":
         
         return cargos(cargo[1],key,leng)
       else:
         if leng == 'Cast':
           return res['result']['speech']
         else:
           return respuestas_bot('error.Salario',leng)

    if intent == 'Impuestos':
        year, barrio, impuesto = res['result']['parameters'].items()
        key = res['result']['action']
        return impuestos_barrio(barrio[1],impuesto[1],year[1],key,leng)
        
  else:
     return respuesta_bot('error.connection',leng)
     
if __name__=='__main__':
  res = sendQuery('valencia',"500737046", 'espanol')
  #print(res)
  if res.status_code == 200:
    
    res = res.json()
    #['result']['resolvedQuery'])
    intent = res['result']['metadata']['intentName']
    if intent == 'inicio':
       geo , date, presu = res['result']['parameters'].items()
       print(date)
       print(presupuesto_general(date[1]))
       








