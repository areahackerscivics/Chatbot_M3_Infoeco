#!/usr/bin/python
##librerias
import logging
from DAO import *
from pymongo import MongoClient
from DAO import addComa
from texto import *
from bson.son import SON
import re

## variable global
client = MongoClient("localhost",27017)
db = client.datos_valencia


def sumaImpuesto(impuesto):
    suma = []
    if impuesto == "impuestos" or impuesto == "impost":
        suma = [
            "$impuestos.IVTNU Personas Físicas",
            "$impuestos.IVTNU Personas Jurídicas",
            "$impuestos.IAE",
            "$impuestos.IVTM Personas Físicas",
            "$impuestos.IVTM Personas Jurídicas",
            "$impuestos.IBI Personas Físicas",
            "$impuestos.IBI Personas Jurídicas"
            ]

    elif impuesto=="IVTNU":
        suma = [
            "$impuestos.IVTNU Personas Físicas",
            "$impuestos.IVTNU Personas Jurídicas"
            ]

    elif impuesto=="IAE":
        suma = [
            "$impuestos.IAE"
            ]

    elif impuesto=="IVTM":
        suma = [
            "$impuestos.IVTM Personas Físicas",
            "$impuestos.IVTM Personas Jurídicas"
            ]

    elif impuesto=="IBI":
        suma = [
            "$impuestos.IBI Personas Físicas",
            "$impuestos.IBI Personas Jurídicas"
            ]

    return suma


def impuestos_barrio(barrio,impuesto,anio,key,leng):
  ##this function return the sum of taxes pay in each neighborhood 
  regx = re.compile("^{}".format(barrio), re.IGNORECASE)
  dbBarrios = db.barrio_impuesto
  if impuesto == '':
     impuesto ='impuestos'
  if anio == '':
    anio = 2016
  else:
    for s in anio.split(): 
      s=s.split('-')
      if s[0].isdigit():
        anio = int(s[0])
  
  if len(list(dbBarrios.find({"anio": anio}))) > 0: ### check if we have data for that year
    pipeline = [
        {"$match": {"sinonimos": regx, "anio": anio}}, #barrio_key
        {"$sort": SON([("anio", -1)])},          ##SON function is use to maintain the sort in python dictionary
        {"$limit": 1},
        {"$project": {
            "_id": "$barrio",
            "valor": {"$sum": []},
            "anyo": "$anio"
            }
         }
        ]

    try:
      suma = sumaImpuesto(impuesto)
    except Exception as e:
      logging.exception("- Error en suma: ")
  

    try:
      ## add taxes that must be added in the pipeline
      pipeline[3]["$project"]["valor"]["$sum"].extend(suma)
    except Exception as e:
      logging.exception("- Error al añadir suma a pipeline: ")
  
    try:
      respuesta = list(dbBarrios.aggregate(pipeline))
      return 1, respuesta_bot(key,leng).format(barrio,addComa(format(respuesta[0]['valor'],"0.2f")),impuesto,anio)
    except Exception as e:
      logging.exception("- Error conexión PagoBarrios: ")
      return 0,respuesta_bot('errorImpRes',leng)
    
  else:
    return 0, respuesta_bot('resErrorano',leng).format(anio)

if __name__ =='__main__':
   print(impuestos_barrio('benimaclet','IBI','2016','res.Impuesto','Cast'))
