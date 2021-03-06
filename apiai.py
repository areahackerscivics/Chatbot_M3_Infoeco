#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import json
import logging
from random import choice
from respuestas.Salarios import *
from texto import *
from respuestas.programa import program
from respuestas.presupuesto import *
from variables import *
from respuestas.impuesto_barrio import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    apiAccess = apiaccess
    apiDeveloperAccess = apiDeveloperaccess

except Exception as e:
    logging.exception("- Error al cargar tokens de api.ai: ")

baseURL = "https://api.dialogflow.com/v1/"
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
        "lifespan": 2
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
  if res.status_code == 200:
    #if we get a answer from Dialogflow, and get the intent to select the answer that we want
    res = res.json()
    #['result']['resolvedQuery'])
    
    intent = res['result']['metadata']['intentName']
    if intent == 'Presupuesto': ## pregunta guardada para proxima iteracion
       geo = res['result']['parameters']['geo-city']
       date= res['result']['parameters']['date-period']
       
       
       return 1, presupuesto_general(geo, date,leng)
       
    if intent == 'Welcome':
       return 0, choice(respuesta_bot(res['result']['action'], leng))
       

    if intent in ['Despedida','bot','comiat']:
       return 0, res['result']['speech']

    if intent in ['Default Fallback Intent']:

       return 0 , respuesta_bot("preg.desconocida", leng) 

    if intent == 'salario':
       cargo = res['result']['parameters']['cargo']
       nombre = res['result']['parameters']['nombre']
       key = res['result']['action']
       if nombre !="":
         return 1, salarios(nombre,key, leng)
       elif cargo !="":
         
         return 1, cargos(cargo,key,leng)
       else:
         if leng == 'Cast':
           return 0, res['result']['speech']
         else:
           return 0, respuestas_bot('error.Salario',leng)

    if intent == 'Impuestos':
        year = res['result']['parameters']['date-period']
        barrio = res['result']['parameters']['barrios']
        impuesto = res['result']['parameters']['Tax']
        key = res['result']['action']
        return  impuestos_barrio(barrio,impuesto,year,key,leng)

    if intent == "Impuesto-context":
        year = res['result']['parameters']['date-period']
        barrio = res['result']['parameters']['barrios']
        impuesto = res['result']['parameters']['Tax']
        key = res['result']['action']
        return  impuestos_barrio(barrio,impuesto,year,key,leng)
    
    if intent == "programas":
        year = res['result']['parameters']['date-period']
        geo = res['result']['parameters']['geo-city']
        return program(year,geo)
        
  else:
     return 0, respuesta_bot('error.connection',leng)
     
if __name__=='__main__':
  res = sendQuery('valencia',"500737046", 'espanol')
  if res.status_code == 200:
    
    res = res.json()
    intent = res['result']['metadata']['intentName']
    if intent == 'inicio':
       geo , date, presu = res['result']['parameters'].items()
       print(date)
       print(presupuesto_general(date[1]))
       








