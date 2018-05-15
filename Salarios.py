#!/usr/bin/python
from pymongo import MongoClient
from texto import *
import re
import logging
from DAO import addComa


client = MongoClient("localhost",27017)
db = client.datos_valencia

def salarios(nombre,key,idioma):
  try:
     # return the salari of high public office
     #se usa expresion regular para que la busqueda coincida incluso si la busqueda no es del todo acertada o hay diferencia en mayusculas
     regx = re.compile("^{}".format(nombre), re.IGNORECASE)
     nomina=list(db.salarios.find({"nombre": regx}))
  except Exception as e:
     logging.exception("error al buscar el nombre del {} alto cargo".format(nombre))
     return respuesta_bot("errorNoResult",idioma)
  if len(nomina) == 0:
     return respuesta_bot("errorNoResult",idioma)
  if len(nomina) == 1:
    return respuesta_bot(key,idioma)[0].format(nombre,addComa(str(nomina[0]['salario'])),nomina[0]['cargo'])
  if len(nomina) > 1:
    return respuesta_bot("errorManyResult",idioma)

def cargos(cargo,key,idioma):
  #this function return the salary of high public office 
  try:
    print(cargo,key)
    nomina=db.salarios.find({"cargo":cargo})
    return respuesta_bot(key,idioma)[1].format(cargo,addComa(str(nomina[0]['salario'])))
    
  except Exception as e:
      logging.exception("error al buscar {} en nuestra base de datos".format(cargo)) 
      return respuesta_bot("errorNoResult",idioma)

if __name__=='__main__':
  print(salarios("María","res.Salario","Cast"))
  

